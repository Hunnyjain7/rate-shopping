from django.db.models.signals import pre_delete
from django.dispatch import receiver

from subscription.models import Subscription, SubscriptionDetail


@receiver(pre_delete, sender=Subscription)
def soft_delete_subscription(sender, instance, **kwargs):  # noqa
    # Soft delete the parent subscription record
    instance.delete()

    # Soft delete child SubscriptionDetail records related to this subscription
    SubscriptionDetail.objects.filter(subscription=instance).update(is_delete=True, is_active=False, is_enable=False)
