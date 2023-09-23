from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import UsrUser


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UsrUser
        fields = '__all__'

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email:
            raise serializers.ValidationError('Email is required.')

        if not password:
            raise serializers.ValidationError('Password is required.')

        return data

    def update(self, instance, validated_data):
        refresh = RefreshToken.for_user(instance)
        access_token = str(refresh.access_token)  # noqa
        instance.token = access_token
        instance.save()
        user_serializer = LoginSerializer(instance)
        return user_serializer.data
