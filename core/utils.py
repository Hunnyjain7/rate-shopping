import random
import uuid
from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.urls import reverse
from faker import Faker

from core.constant import GROUPS, SYSTEM

faker = Faker()


def get_uuid():
    return uuid.uuid4


def get_random_number():
    return str(random.randint(0, 99999999))


def get_group(name):
    group = Group.objects.filter(name=name)
    return group.first() if group.exists() else None


def get_authenticated_user(context):
    return context["request"].user if "request" in context else None


def get_today_datetime():
    return datetime.now()


def create_client_name(user):
    return f"{user.first_name} {user.last_name}".title()


def get_error_data(error="Operation failed."):
    return {"error": error}


def get_response_data(data=dict):
    return {"data": data}


def get_user_login_url(user_role):
    return "/api" + reverse(f"{user_role.lower()}:login")


def create_test_user(user_role):
    admin_group = get_group(GROUPS[user_role])
    permissions = Permission.objects.all()
    admin_group.permissions.set(permissions)

    extra_fields = {
        "created_by": SYSTEM,
        "updated_by": SYSTEM,
        "display_name": f"{user_role} Test Case",
        "first_name": f"{user_role} Test",
        "last_name": "Case",
        "is_default": True,
        "is_it_admin": True,
        "user_type_term": user_role,
    }
    user_email = f"{user_role.lower()}testcase@gmail.com"
    user_password = f"Test{user_role}@123"
    user_instance = get_user_model().objects.create_user(
        user_email, user_password, **extra_fields
    )
    user_instance.save()
    return user_email, user_password


def test_user_login(client, user_role):
    user_email, user_password = create_test_user(user_role)
    login_url = get_user_login_url(user_role)
    login_data = {"email": user_email, "password": user_password}
    response = client.post(login_url, data=login_data)
    response_data = response.json()
    user_instance = get_user_model().objects.get(id=response_data["data"]["id"])
    return user_instance


def get_faker():
    return faker


def generate_phone_number(country_code="+91", prefix="98", number_length=8):
    phone_number = faker.phone_number()  # Get a random phone number
    # Extract only the digits from the phone number
    digits = "".join(filter(str.isdigit, phone_number))
    phone_number = f"{country_code}{prefix}{digits[:number_length]}"
    return phone_number


def create_client(client, url):
    client_data = {
        "contact_name": SYSTEM,
        "email": faker.email(),
        "username": faker.user_name(),
        "password": faker.password(),
        "address_line_one": faker.address(),
        "address_line_two": faker.address(),
        "city": faker.city(),
        "state": faker.state(),
        "country": faker.country(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "mobile_number": generate_phone_number(),
    }
    return client.post(url, data=client_data)
