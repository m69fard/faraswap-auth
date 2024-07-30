from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


# Create your tests here.
class TestAuthentication(APITestCase):

    def setUp(self):
        User.objects.create_user(
            username="current_user",
            password="pass",
            phone_number="1234567890",
        )

    def test_register(self):
        url = reverse("register")
        response = self.client.post(
            url, data={"username": "new_user", "password": "pass", "phone_number": "09121002030"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        url = reverse("login")
        response = self.client.post(
            url,
            data={
                "username": "current_user",
                "password": "pass",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
