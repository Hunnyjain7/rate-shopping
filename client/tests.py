from rest_framework.reverse import reverse

from client.models import Client
from core.tests import BaseAPITestCase
from core.utils import create_client


class ClientViewSetTestCase(BaseAPITestCase):
    reverse_param = "client-user-list"

    def test_create_client_user(self):
        client_response = create_client(self.client, self.url)
        client_data = client_response.json()
        client_instance = Client.objects.get(id=client_data["data"]["id"])
        self.assertIsInstance(client_instance, Client)
        self.assertEqual(client_response.status_code, self.status.HTTP_201_CREATED)
        self.assertEqual(client_data["status"], self.success)

    def test_list_client_users(self):
        response = self.client.get(self.url)
        response_data = response.json()
        self.assertEqual(response.status_code, self.status.HTTP_200_OK)
        self.assertEqual(response_data["status"], self.success)

    def test_retrieve_client_user(self):
        client_response = create_client(self.client, self.url)
        client_data = client_response.json()
        client_id = client_data["data"]["id"]
        detail_url = reverse("client-user-detail", args=[client_id])
        response = self.client.get(detail_url)
        response_data = response.json()
        self.assertEqual(response_data["status"], self.success)
        self.assertEqual(response.status_code, self.status.HTTP_200_OK)

    def test_partial_update_client_user(self):
        client_response = create_client(self.client, self.url)
        client_data = client_response.json()
        client_id = client_data["data"]["id"]
        update_url = reverse("client-user-detail", args=[client_id])
        partial_data = {"first_name": self.faker.first_name()}
        response = self.client.patch(update_url, data=partial_data)
        response_data = response.json()
        self.assertEqual(response_data["status"], self.success)
        self.assertEqual(
            response_data["data"]["user"]["first_name"], partial_data["first_name"]
        )
        self.assertEqual(response.status_code, self.status.HTTP_200_OK)

    def test_destroy_action(self):
        client_response = create_client(self.client, self.url)
        client_data = client_response.json()
        client_id = client_data["data"]["id"]
        destroy_url = reverse("client-user-detail", args=[client_id])
        response = self.client.delete(destroy_url)
        self.assertEqual(response.status_code, self.status.HTTP_204_NO_CONTENT)
