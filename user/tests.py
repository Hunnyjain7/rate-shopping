from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from core.tests import BaseAPITestCase
from core.utils import generate_phone_number


class UsrUserViewSetTestCase(BaseAPITestCase):
    reverse_param = "user-list"

    def test_create_admin_user(self):
        user_data = {
            "email": self.faker.email(),
            "password": self.faker.password(),
            "username": self.faker.user_name(),
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "mobile_number": generate_phone_number(),
        }
        response = self.client.post(self.url, data=user_data)
        response_data = response.json()
        self.user_instance = get_user_model().objects.get(
            id=response_data["data"]["id"]
        )
        self.assertEqual(response.status_code, self.status.HTTP_201_CREATED)
        self.assertEqual(response_data["status"], self.success)

    def test_list_admin_users(self):
        response = self.client.get(self.url)
        response_data = response.json()
        self.assertGreater(response_data["data"]["count"], 0)
        self.assertEqual(response.status_code, self.status.HTTP_200_OK)
        self.assertEqual(response_data["status"], self.success)

    def test_retrieve_admin_user(self):
        detail_url = reverse("user-detail", args=[self.user_instance.id])
        response = self.client.get(detail_url)
        response_data = response.json()
        self.assertEqual(response_data["status"], self.success)
        self.assertEqual(response.status_code, self.status.HTTP_200_OK)

    def test_partial_update_admin_user(self):
        update_url = reverse("user-detail", args=[self.user_instance.id])
        partial_data = {"last_name": self.faker.last_name()}
        response = self.client.patch(update_url, data=partial_data)
        response_data = response.json()
        self.assertEqual(response_data["status"], self.success)
        self.assertEqual(response_data["data"]["last_name"], partial_data["last_name"])
        self.assertEqual(response.status_code, self.status.HTTP_200_OK)

    def test_destroy_admin_user(self):
        destroy_url = reverse("user-detail", args=[self.user_instance.id])
        response = self.client.delete(destroy_url)
        self.assertEqual(response.status_code, self.status.HTTP_204_NO_CONTENT)
