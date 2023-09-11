from django.db import models

from client.models import Client
from core.models import ActiveDeleteModel, BaseActivationRenewal, BaseActiveDeleteModel
from core.utils import get_random_number, get_uuid


# Create your models here.
class MaxCCP(models.Model):
    """Max Competitors, Corporates and Property"""

    max_competitors = models.PositiveIntegerField(default=0)
    max_corporates = models.PositiveIntegerField(default=0)
    max_properties = models.PositiveIntegerField(default=0)
    max_users = models.PositiveIntegerField(default=0)
    is_marriott_enable = models.BooleanField(default=False)
    is_ihg_enable = models.BooleanField(default=False)
    is_hilton_enable = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    update_log = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subscription(BaseActiveDeleteModel):
    name = models.CharField(max_length=69)
    short_description = models.CharField(max_length=361, null=True, blank=True)
    detail_description = models.TextField()
    subscription_image = models.FileField(
        upload_to="media/images/subscription_images", null=True, blank=True
    )
    monthly_amount = models.DecimalField(decimal_places=2, max_digits=15)
    yearly_amount = models.DecimalField(decimal_places=2, max_digits=15)
    discount = models.DecimalField(decimal_places=2, max_digits=15)
    order_number = models.PositiveIntegerField(
        unique=True, editable=False, serialize=True, auto_created=True
    )


class SubscriptionDetail(MaxCCP, ActiveDeleteModel):
    id = models.UUIDField(primary_key=True, default=get_uuid(), editable=False)
    subscription = models.ForeignKey(Subscription, on_delete=models.DO_NOTHING)
    upto_corporate_group_term = models.CharField(max_length=67, null=True, blank=True)
    is_enable = models.BooleanField(default=False)
    update_log = models.DateTimeField(auto_now=True)


class ClientSubscription(BaseActivationRenewal):
    id = models.UUIDField(primary_key=True, default=get_uuid(), editable=False)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    subscription = models.ForeignKey(Subscription, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=69)
    date_of_purchase = models.DateTimeField()
    subscription_amount = models.DecimalField(decimal_places=2, max_digits=15)
    paid_amount = models.DecimalField(decimal_places=2, max_digits=15)
    ref_transaction_number = models.CharField(max_length=367, null=True, blank=True)
    due_date = models.DateTimeField()
    status_term = models.CharField(max_length=39, null=True, blank=True)
    invoice_ref_number = models.CharField(
        max_length=39, default=f"INV-REF-{get_random_number()}", editable=False
    )
    is_active = models.BooleanField(default=False)
    update_log = models.DateTimeField(auto_now=True)
    seq_number = models.PositiveIntegerField(
        unique=True, editable=False, serialize=True, auto_created=True
    )
    is_reconcile = models.BooleanField(default=False)
    transaction_status_term = models.CharField(max_length=39, null=True, blank=True)
    subscription_type_term = models.CharField(max_length=39, null=True, blank=True)
    ref_client_subscription = models.ForeignKey(
        "self", default=None, null=True, on_delete=models.DO_NOTHING
    )
    main_amount = models.DecimalField(decimal_places=2, max_digits=15)
    discount = models.DecimalField(decimal_places=2, max_digits=15)


class ClientSubscriptionDetail(MaxCCP):
    id = models.UUIDField(primary_key=True, default=get_uuid(), editable=False)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    subscription = models.ForeignKey(Subscription, on_delete=models.DO_NOTHING)
    client_subscription = models.ForeignKey(
        ClientSubscription, on_delete=models.DO_NOTHING
    )
    actual_competitors = models.PositiveIntegerField(default=0)
    actual_corporates = models.PositiveIntegerField(default=0)
    actual_properties = models.PositiveIntegerField(default=0)
    actual_users = models.PositiveIntegerField(default=0)
    is_ihg_in_use = models.BooleanField(default=False)
    is_marriott_in_use = models.BooleanField(default=False)
    is_hilton_in_use = models.BooleanField(default=False)
    seq_number = models.PositiveIntegerField(
        unique=True, editable=False, serialize=True, auto_created=True
    )
