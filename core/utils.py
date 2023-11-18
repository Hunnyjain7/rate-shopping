import random
import uuid
from datetime import datetime

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


def get_authenticated_user(context):
    if "request" in context:
        return context["request"].user
    return


def get_today_datetime():
    return datetime.now()


def create_client_name(user):
    return f"{user.first_name} {user.last_name}".title()


def get_error_data(error="Operation failed."):
    return {"error": error}


def get_response_data(data=dict):
    return {"data": data}
