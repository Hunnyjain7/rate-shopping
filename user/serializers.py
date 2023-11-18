from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from core.constant import ADMIN
from core.utils import get_authenticated_user
from user.models import UsrUser


class UsrUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, min_length=8, max_length=15, required=True
    )

    restricted_fields = [
        "id",
        "seq_number",
        "is_superuser",
        "is_active",
        "is_delete",
        "association_id",
        "association_type_term",
        "user_type_term",
        "client_id",
        "email",
        "username",
        "is_staff",
        "is_default",
        "is_it_admin",
    ]

    class Meta:
        model = UsrUser
        fields = "__all__"

    def validate(self, data):
        # Check if any restricted field is present in the data for update
        if self.instance:
            for field in self.restricted_fields:
                if field in data:
                    raise serializers.ValidationError(
                        f"{field} cannot be inserted or updated."
                    )
        return super().validate(data)

    def validate_password(self, value):
        # Use Django's built-in password validators
        try:
            password_validation.validate_password(value, self.instance)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(str(exc))

        return value

    def save(self, **kwargs):
        auth_user = get_authenticated_user(self.context)
        self.validated_data["updated_by"] = auth_user.id

        if self.validated_data.get("password"):
            self.validated_data["password"] = make_password(
                self.validated_data["password"]
            )

        if not self.instance:
            if self.validated_data.get("profile_image"):
                raise serializers.ValidationError(
                    "Profile pic can be updated separately."
                )
            self.validated_data["user_type_term"] = kwargs.get("user_type_term", ADMIN)
            self.validated_data["association_type_term"] = kwargs.get(
                "association_type_term"
            )
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
