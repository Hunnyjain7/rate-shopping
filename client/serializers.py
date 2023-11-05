from rest_framework import serializers

from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = (
            "date_of_activation",
            "date_of_renewal",
            "address",
            "activation_by",
            "user",
        )
