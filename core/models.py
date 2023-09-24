from django.db import models

from core.utils import get_uuid


# Create your models here.
class ActiveDeleteModel(models.Model):
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        # Set abstract to True to prevent migrations for this base model
        abstract = True

    def delete(self):  # noqa
        """Mark the record as deleted instead of deleting it"""

        self.is_delete = True
        self.is_active = False
        self.save()


class BaseModel(models.Model):
    # Common fields that you want in all models
    id = models.UUIDField(primary_key=True, default=get_uuid(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=38, null=True, blank=True)
    updated_by = models.CharField(max_length=38, null=True, blank=True)

    class Meta:
        # Set abstract to True to prevent migrations for this base model
        abstract = True


class BaseActiveDeleteModel(ActiveDeleteModel, BaseModel):
    class Meta:
        abstract = True


class Association(models.Model):
    association_id = models.CharField(max_length=38, null=True, blank=True)
    association_type_term = models.CharField(max_length=39, null=True, blank=True)

    class Meta:
        # Set abstract to True to prevent migrations for this base model
        abstract = True


class Address(Association):
    id = models.UUIDField(primary_key=True, default=get_uuid(), editable=False)
    address_line_one = models.CharField(max_length=367, null=True, blank=True)
    address_line_two = models.CharField(max_length=367, null=True, blank=True)
    city = models.CharField(max_length=39, null=True, blank=True)
    state = models.CharField(max_length=39, null=True, blank=True)
    country = models.CharField(max_length=39, null=True, blank=True)
    is_delete = models.BooleanField(default=False)

    def delete(self):  # noqa
        """Mark the record as deleted instead of deleting it"""

        self.is_delete = True
        self.save()


class BaseActivationRenewal(models.Model):
    date_of_activation = models.DateTimeField()
    date_of_renewal = models.DateTimeField()

    class Meta:
        # Set abstract to True to prevent migrations for this base model
        abstract = True
