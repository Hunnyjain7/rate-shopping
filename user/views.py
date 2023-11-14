from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.constant import ADMIN
from core.pagination import CustomPagination
from core.permissions import is_in_group_factory
from core.views import BaseModelViewSet

from user.models import UsrUser
from user.serializers import LoginSerializer, UsrUserSerializer


class UsrUserViewSet(BaseModelViewSet):
    queryset = UsrUser.objects.filter(is_delete=False, is_active=True, user_type_term=ADMIN).order_by('-seq_number')
    serializer_class = UsrUserSerializer
    allowed_groups = [ADMIN]
    permission_classes = [IsAuthenticated, is_in_group_factory(allowed_groups)]
    pagination_class = CustomPagination
    success_messages = {
        'create': "User created successfully.",
        'update': "User updated successfully.",
        'retrieve': "User detail's fetched successfully.",
        'list': "User's data fetched successfully.",
        'destroy': "User deleted successfully.",
        'partial_update': "User updated successfully."
    }

    def perform_destroy(self, instance):
        instance.delete(updated_by=self.request.user.id)


class LoginViewSet(UsrUserViewSet):
    serializer_class = LoginSerializer
    success_messages = {
        'create': "User logged in successfully."
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
                {"error": "Authentication failed. Check your email and password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        user_data = serializer.update(user, validated_data)
        return Response({"data": user_data})
