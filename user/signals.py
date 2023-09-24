from django.db.models.signals import post_save
from django.dispatch import receiver

from core.constant import ADMIN, GROUPS
from core.utils import get_group
from user.models import UsrUser


@receiver(post_save, sender=UsrUser)
def add_user_to_group(sender, instance, created, **kwargs):  # noqa
    # Check if the user instance was just created
    if created and not instance.groups.exists():
        instance.groups.add(get_group(GROUPS[ADMIN]))
