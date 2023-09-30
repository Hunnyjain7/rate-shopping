from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.constant import ADMIN
from core.pagination import CustomPagination
from core.permissions import is_in_group_factory
from user.models import UsrUser
from user.serializers import LoginSerializer, UsrUserSerializer


class UsrUserViewSet(viewsets.ModelViewSet):
    queryset = UsrUser.objects.filter(is_delete=False, is_active=True)
    serializer_class = UsrUserSerializer
    allowed_groups = [ADMIN]
    permission_classes = [IsAuthenticated, is_in_group_factory(allowed_groups)]
    pagination_class = CustomPagination

    def perform_destroy(self, instance):
        instance.delete(updated_by=self.request.user.id)


class LoginViewSet(UsrUserViewSet):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

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
        return Response(
            {"message": "Logged in successfully", "data": user_data},
            status=status.HTTP_200_OK,
        )
