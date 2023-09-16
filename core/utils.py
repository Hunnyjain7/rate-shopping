import random
import uuid

from django.contrib.auth.models import Group


def get_uuid():
    return uuid.uuid4


def get_random_number():
    return str(random.randint(0, 99999999))


def get_group(name):
    group = Group.objects.filter(name=name)
    if group.exists():
        return group.first()
    return
