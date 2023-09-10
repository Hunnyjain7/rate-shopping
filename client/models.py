from django.db import models

from core.models import BaseActiveDeleteModel, BaseActivationRenewal, Address
from core.utils import get_random_number
from user.models import UsrUser


# Create your models here.
class Client(BaseActiveDeleteModel, BaseActivationRenewal):
    client_name = models.CharField(max_length=350)
    code = models.CharField(max_length=15, default=f"CLI{get_random_number()}", editable=False)
    contact_name = models.CharField(max_length=350, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    date_of_registration = models.DateTimeField(editable=False)
    client_status_term = models.CharField(max_length=39, null=True, blank=True)
    activation_by = models.ForeignKey(UsrUser, on_delete=models.DateField, related_name="activation_by")
    relation_manager_id = models.CharField(max_length=39, null=True, blank=True)
    total_competitors = models.PositiveIntegerField(default=0)
    total_corporates = models.PositiveIntegerField(default=0)
    total_properties = models.PositiveIntegerField(default=0)
    last_contacted = models.DateTimeField(null=True, blank=True)
    user = models.OneToOneField(UsrUser, on_delete=models.DO_NOTHING)
    is_enable = models.BooleanField(default=False)
    seq_number = models.PositiveIntegerField(unique=True, editable=False, serialize=True, auto_created=True)
