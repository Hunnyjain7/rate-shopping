from django.db import models
from django.db.models import Max

from core.models import Address, BaseActivationRenewal, BaseActiveDeleteModel
from core.utils import get_random_number
from user.models import UsrUser


# Create your models here.
class Client(BaseActiveDeleteModel, BaseActivationRenewal):
    client_name = models.CharField(max_length=350)
    code = models.CharField(max_length=15, editable=False)
    contact_name = models.CharField(max_length=350, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    date_of_registration = models.DateTimeField(auto_now=True, editable=False)
    client_status_term = models.CharField(max_length=39, null=True, blank=True)
    activation_by = models.ForeignKey(
        UsrUser, on_delete=models.DateField, related_name="activation_by"
    )
    relation_manager_id = models.CharField(max_length=39, null=True, blank=True)
    total_competitors = models.PositiveIntegerField(default=0)
    total_corporates = models.PositiveIntegerField(default=0)
    total_properties = models.PositiveIntegerField(default=0)
    last_contacted = models.DateTimeField(null=True, blank=True)
    user = models.OneToOneField(UsrUser, on_delete=models.DO_NOTHING)
    is_enable = models.BooleanField(default=True)
    seq_number = models.PositiveIntegerField(
        unique=True, editable=False, serialize=True, auto_created=True
    )

    @staticmethod
    def get_seq_number():
        obj = Client.objects.aggregate(max_value=Max("seq_number"))
        obj["max_value"] = 0 if obj["max_value"] is None else obj["max_value"]
        return obj["max_value"] + 1

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = f"CLI{get_random_number()}"
        if not self.seq_number:
            self.seq_number = self.get_seq_number()
        if not self.created_by:
            self.created_by = self.updated_by
        super(Client, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Mark the record as deleted instead of deleting it"""
        self.updated_by = kwargs.pop("updated_by")
        super().delete()
