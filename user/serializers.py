from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from core.constant import ADMIN
from core.utils import get_authenticated_user_id
from user.models import UsrUser


class UsrUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UsrUser
        fields = "__all__"

    def save(self, **kwargs):
        auth_user = get_authenticated_user_id(self.context)
        self.validated_data["updated_by"] = auth_user

        if self.validated_data.get("password"):
            self.validated_data["password"] = make_password(
                self.validated_data["password"]
            )

        if not self.instance:
            if self.validated_data.get("profile_image"):
                raise serializers.ValidationError(
                    "Profile pic can be updated separately."
                )
            self.validated_data["association_id"] = auth_user
            self.validated_data["user_type_term"] = ADMIN
            self.validated_data["association_type_term"] = ADMIN
        return super().save(**kwargs)


class LoginSerializer(UsrUserSerializer):
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email:
            raise serializers.ValidationError("Email is required.")

        if not password:
            raise serializers.ValidationError("Password is required.")

        return data

    def update(self, instance, validated_data):
        refresh = RefreshToken.for_user(instance)
        access_token = str(refresh.access_token)  # noqa
        instance.token = access_token
        instance.save()
        user_serializer = UsrUserSerializer(instance)
        return user_serializer.data
