from django.contrib.auth.models import Permission
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from core.constant import GROUPS, ADMIN, SUCCESS
from core.utils import get_group
from user.models import UsrUser


class UsrUserViewSetTestCase(APITestCase):
    def setUp(self):
        # Set up any necessary data for your tests
        admin_group = get_group(GROUPS[ADMIN])
        permissions = Permission.objects.all()
        admin_group.permissions.set(permissions)

        extra_fields = {
            "created_by": "system",
            "updated_by": "system",
            "display_name": "Test",
            "first_name": "Test",
            "last_name": "Case",
            "is_default": True,
            "is_it_admin": True,
            "user_type_term": ADMIN
        }
        self.user_instance = UsrUser.objects.create_superuser(
            "testcase@gmail.com", "Test@123", **extra_fields
        )
        refresh = RefreshToken.for_user(self.user_instance)
        access_token = str(refresh.access_token)  # noqa
        self.user_instance.token = access_token
        self.user_instance.save()
        self.url = reverse('user-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_instance.token}')

    def test_create_admin_user(self):
        user_data = {
            "email": "test1@gmail.com",
            "password": "111n12uaa",
            "username": "test20",
            "first_name": "Test",
            "last_name": "20",
            "mobile_number": "+917897777897"
        }
        response = self.client.post(self.url, data=user_data)
        response_data = response.json()
        self.user_instance = UsrUser.objects.get(id=response_data["data"]["id"])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data["status"], SUCCESS)

    def test_list_admin_users(self):
        response = self.client.get(self.url)
        response_data = response.json()
        self.assertGreater(response_data["data"]["count"], 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["status"], SUCCESS)

    def test_retrieve_admin_user(self):
        detail_url = reverse('user-detail', args=[self.user_instance.id])
        response = self.client.get(detail_url)
        response_data = response.json()
        self.assertEqual(response_data["status"], SUCCESS)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_admin_user(self):
        update_url = reverse('user-detail', args=[self.user_instance.id])
        partial_data = {
            "last_name": "updated last_name"
        }
        response = self.client.patch(update_url, data=partial_data)
        response_data = response.json()
        self.assertEqual(response_data["status"], SUCCESS)
        self.assertEqual(response_data["data"]["last_name"], partial_data["last_name"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_admin_user(self):
        destroy_url = reverse('user-detail', args=[self.user_instance.id])
        response = self.client.delete(destroy_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
