from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import Max
from phonenumber_field.modelfields import PhoneNumberField

from core.models import Association, BaseActiveDeleteModel


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("seq_number", UsrUser.get_seq_number())

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class UsrUser(AbstractBaseUser, Association, BaseActiveDeleteModel, PermissionsMixin):
    client_id = models.UUIDField(max_length=38, null=True, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=61, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    token = models.TextField(null=True, blank=True)
    status_term = models.CharField(max_length=39, null=True, blank=True)
    profile_image = models.FileField(
        upload_to="media/images/profile_images", null=True, blank=True
    )
    display_name = models.CharField(max_length=61, null=True, blank=True)
    mobile_number = PhoneNumberField(blank=True, null=True)
    seq_number = models.PositiveIntegerField(
        unique=True, editable=False, serialize=True, auto_created=True
    )
    user_type_term = models.CharField(max_length=39, null=True, blank=True)
    is_default = models.BooleanField(default=False)
    is_it_admin = models.BooleanField(default=False)
    forget_password_token = models.TextField(null=True, blank=True)

    # Add your custom fields here

    objects = UserManager()

    USERNAME_FIELD = "email"

    @staticmethod
    def get_seq_number():
        obj = UsrUser.objects.aggregate(max_value=Max("seq_number"))
        obj["max_value"] = 0 if obj["max_value"] is None else obj["max_value"]
        return obj["max_value"] + 1

    def save(self, *args, **kwargs):
        if not self.display_name:
            display_name = self.username
            if self.first_name and self.last_name:
                display_name = f"{self.first_name} {self.last_name}"
            self.display_name = display_name.title()
        if not self.created_by:
            self.created_by = self.updated_by
        if not self.seq_number:
            self.seq_number = self.get_seq_number()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Mark the record as deleted instead of deleting it"""
        self.updated_by = kwargs.pop("updated_by")
        self.is_delete = True
        self.is_active = False
        super().save(*args, **kwargs)
