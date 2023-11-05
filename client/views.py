from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from client.models import Client
from client.serializers import ClientSerializer
from core.constant import ADMIN
from core.pagination import CustomPagination
from core.permissions import is_in_group_factory


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(is_enable=True, is_delete=False, is_active=True)
    serializer_class = ClientSerializer
    allowed_groups = [ADMIN]
    permission_classes = [IsAuthenticated, is_in_group_factory(allowed_groups)]
    pagination_class = CustomPagination

    def perform_destroy(self, instance):
        instance.delete(updated_by=self.request.user.id)
