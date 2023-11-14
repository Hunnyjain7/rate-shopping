from rest_framework.permissions import IsAuthenticated

from client.models import Client
from client.serializers import ClientSerializer

from core.constant import ADMIN
from core.pagination import CustomPagination
from core.permissions import is_in_group_factory
from core.views import BaseModelViewSet


class ClientViewSet(BaseModelViewSet):
    queryset = Client.objects.filter(
        is_enable=True, is_delete=False, is_active=True, user__is_delete=False, address__is_delete=False
    ).order_by('-seq_number')
    serializer_class = ClientSerializer
    allowed_groups = [ADMIN]
    permission_classes = [IsAuthenticated, is_in_group_factory(allowed_groups)]
    pagination_class = CustomPagination
    success_messages = {
        'create': "Client created successfully.",
        'update': "Client updated successfully.",
        'retrieve': "Client detail's fetched successfully.",
        'list': "Client's data fetched successfully.",
        'destroy': "Client deleted successfully.",
        'partial_update': "Client updated successfully."
    }

    def perform_destroy(self, instance):
        updated_by = self.request.user.id
        instance.address.delete()
        instance.user.delete(updated_by=updated_by)
        instance.delete(updated_by=updated_by)
