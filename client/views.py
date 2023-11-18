from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from client.models import Client
from client.serializers import ClientLoginSerializer, ClientSerializer
from core.constant import ADMIN, CLIENT
from core.pagination import CustomPagination
from core.permissions import is_in_group_factory
from core.utils import get_error_data, get_response_data
from core.views import BaseModelViewSet


class ClientViewSet(BaseModelViewSet):
    queryset = Client.objects.filter(
        is_enable=True,
        is_delete=False,
        is_active=True,
        user__is_delete=False,
        address__is_delete=False,
        user__groups__name=CLIENT,
    ).order_by("-seq_number")
    serializer_class = ClientSerializer
    allowed_groups = [ADMIN]
    permission_classes = [IsAuthenticated, is_in_group_factory(allowed_groups)]
    pagination_class = CustomPagination
    success_messages = {
        "create": "Client created successfully.",
        "update": "Client updated successfully.",
        "retrieve": "Client detail's fetched successfully.",
        "list": "Client's data fetched successfully.",
        "destroy": "Client deleted successfully.",
        "partial_update": "Client updated successfully.",
    }

    def perform_destroy(self, instance):
        updated_by = self.request.user.id
        instance.address.delete()
        instance.user.delete(updated_by=updated_by)
        instance.delete(updated_by=updated_by)


class ClientLoginViewSet(ClientViewSet):
    serializer_class = ClientLoginSerializer
    success_messages = {"create": "Client logged in successfully."}
    error_messages = {
        "create": "Client login failed.",
    }

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            allowed_groups = [ADMIN]
            permission_classes = [IsAuthenticated, is_in_group_factory(allowed_groups)]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)
        validated_data = serializer.validate(request.data)
        email = validated_data["email"]
        password = validated_data["password"]
        user = authenticate(request, email=email, password=password)
        if not user:
            return Response(
                get_error_data("Authentication failed. Check your email and password."),
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if not user.groups.filter(name=CLIENT).exists():
            return Response(
                get_error_data("You don't have permission for client login."),
                status=status.HTTP_403_FORBIDDEN,
            )

        user_data = serializer.update(user, validated_data)
        return Response(get_response_data(user_data))
