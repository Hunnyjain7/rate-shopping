from django.contrib.auth import authenticate

from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import viewsets, status
from rest_framework.response import Response

from user.models import UsrUser
from user.serializers import LoginSerializer


class LoginViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = UsrUser
    serializer_class = LoginSerializer

    @action(detail=False, methods=['GET'])
    def login(self, request):
        serializer = self.serializer_class(request.query_params)
        validated_data = serializer.validate(request.query_params)
        email = validated_data['email']
        password = validated_data['password']
        user = authenticate(request, email=email, password=password)
        if not user:
            return Response(
                {'error': 'Authentication failed. Check your email and password.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        user_data = serializer.update(user, validated_data)
        return Response({"message": "Logged in successfully", "data": user_data}, status=status.HTTP_200_OK)
