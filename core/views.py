from rest_framework import viewsets

from core.mixins import SuccessMessageMixin


# Create your views here.
class BaseModelViewSet(SuccessMessageMixin, viewsets.ModelViewSet):
    pass
