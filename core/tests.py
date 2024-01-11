from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.constant import ADMIN, SUCCESS
from core.utils import get_faker, test_user_login


class BaseAPITestCase(APITestCase):
    reverse_param = "api"
    user_role = ADMIN
    success = SUCCESS
    status = status

    def setUp(self):
        # Set up any necessary data for your tests
        self.faker = get_faker()
        self.user_instance = test_user_login(self.client, self.user_role)
        self.url = self.create_reverse_base_url()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_instance.token}")

    def create_reverse_base_url(self):
        return reverse(self.reverse_param)
