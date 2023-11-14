from rest_framework import serializers

from client.models import Client
from core.constant import CLIENT
from core.serializers import AddressSerializer
from core.utils import get_authenticated_user, create_client_name

from user.serializers import UsrUserSerializer


class ClientSerializer(serializers.ModelSerializer):
    address_line_one = serializers.CharField(write_only=True, required=True)
    address_line_two = serializers.CharField(write_only=True, required=False)
    city = serializers.CharField(write_only=True, required=True)
    state = serializers.CharField(write_only=True, required=True)
    country = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)
    client_name = serializers.CharField(required=False)
    profile_image = serializers.FileField(write_only=True, required=False, allow_null=True, allow_empty_file=True)
    mobile_number = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, min_length=8, max_length=15, required=True)

    restricted_fields = [
        'id',
        'code',
        'client_name',
        'is_superuser',
        'is_staff',
        'is_delete',
        'is_enable',
        'last_login',
        'seq_number',
        'token'
    ]

    class Meta:
        model = Client
        exclude = ('address', 'activation_by', 'user')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        user_representation = UsrUserSerializer(instance.user).data
        address_representation = AddressSerializer(instance.address).data
        response["user"] = user_representation
        response["address"] = address_representation
        return response

    def validate(self, data):
        # Check if any restricted field is present in the data for update
        if self.instance:
            for field in self.restricted_fields:
                if field in data:
                    raise serializers.ValidationError(f"{field} cannot be updated.")
        return super().validate(data)

    @staticmethod
    def get_address_data(validated_data, instance=None):
        fields = ['address_line_one', 'address_line_two', 'city', 'state', 'country']
        return {
            field: validated_data.pop(field, getattr(instance, field, None)) for field in fields if
            field in validated_data
        }

    @staticmethod
    def get_user_data(validated_data, instance=None):
        fields = ['email', 'username', 'first_name', 'last_name', 'profile_image', 'mobile_number', 'password']
        return {
            field: validated_data.pop(field, getattr(instance, field, None)) for field in fields if
            field in validated_data
        }

    def create(self, validated_data):
        address_data = self.get_address_data(validated_data)
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address_instance = address_serializer.save()

        user_data = self.get_user_data(validated_data)
        user_serializer = UsrUserSerializer(data=user_data, context=self.context)
        user_serializer.is_valid(raise_exception=True)
        user_instance = user_serializer.save(user_type_term=CLIENT, association_type_term=CLIENT)

        auth_user = get_authenticated_user(self.context)
        validated_data["activation_by"] = auth_user
        validated_data["updated_by"] = auth_user.id
        validated_data['address'] = address_instance
        validated_data['user'] = user_instance
        validated_data["is_active"] = True
        validated_data["is_enable"] = True
        validated_data["client_name"] = create_client_name(user_instance)
        client_instance = Client.objects.create(**validated_data)

        user_instance.association_id = client_instance.id
        user_instance.client_id = client_instance.id
        user_instance.save()
        address_instance.association_id = client_instance.id
        address_instance.association_type_term = CLIENT
        address_instance.save()
        return client_instance

    def update(self, instance, validated_data):
        address_instance = instance.address
        address_data = self.get_address_data(validated_data, address_instance)
        address_serializer = AddressSerializer(address_instance, data=address_data, partial=True)
        address_serializer.is_valid(raise_exception=True)
        address_serializer.save()

        user_instance = instance.user
        user_data = self.get_user_data(validated_data, user_instance)
        user_serializer = UsrUserSerializer(user_instance, data=user_data, context=self.context, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()

        for field in instance._meta.fields:  # noqa
            field_name = field.name
            if field_name in validated_data:
                setattr(instance, field_name, validated_data[field_name])
        instance.save()
        return instance
