from rest_framework import serializers

from .models import (
    ClientSubscription,
    ClientSubscriptionDetail,
    Subscription,
    SubscriptionDetail,
)


class SubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionDetail
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class SubscriptionSerializer(serializers.ModelSerializer):
    subscription_details = SubscriptionDetailSerializer(many=False, read_only=True)
    final_amount = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = "__all__"
        read_only_fields = ("order_number", "created_at", "updated_at")

    def get_final_amount(self, obj):
        # Calculate final amount based on percentage discount
        discount_amount = (obj.monthly_amount * obj.discount) / 100
        return obj.monthly_amount - discount_amount

    def validate_image(self, value):
        if not value:
            raise serializers.ValidationError("Image is required.")
        return value


class ClientSubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSubscriptionDetail
        fields = "__all__"
        read_only_fields = ("id", "seq_number", "created_at", "updated_at")


class ClientSubscriptionSerializer(serializers.ModelSerializer):
    client_subscription_details = ClientSubscriptionDetailSerializer(
        many=False, read_only=True
    )
    final_amount = serializers.SerializerMethodField()

    class Meta:
        model = ClientSubscription
        fields = "__all__"
        read_only_fields = (
            "id",
            "invoice_ref_number",
            "seq_number",
            "created_at",
            "updated_at",
        )

    def get_final_amount(self, obj):
        # Calculate final amount based on percentage discount
        discount_amount = (obj.main_amount * obj.discount) / 100
        return obj.main_amount - discount_amount

    def validate_image(self, value):
        if not value:
            raise serializers.ValidationError("Image is required.")
        return value
