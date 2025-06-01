from rest_framework import viewsets

from core.mixins import BaseModelViewSet

from .models import ClientSubscription, Subscription
from .serializers import ClientSubscriptionSerializer, SubscriptionSerializer


class SubscriptionViewSet(BaseModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.success_response(
            serializer.data, "Subscription retrieved successfully."
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.success_response(
            serializer.data, "Subscription created successfully.", status=201
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return self.success_response(
            serializer.data, "Subscription updated successfully."
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return self.success_response(
            {}, "Subscription deleted successfully.", status=204
        )


class ClientSubscriptionViewSet(BaseModelViewSet):
    queryset = ClientSubscription.objects.all()
    serializer_class = ClientSubscriptionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.success_response(
            serializer.data, "Client Subscription retrieved successfully."
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.success_response(
            serializer.data, "Client Subscription created successfully.", status=201
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return self.success_response(
            serializer.data, "Client Subscription updated successfully."
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return self.success_response(
            {}, "Client Subscription deleted successfully.", status=204
        )
