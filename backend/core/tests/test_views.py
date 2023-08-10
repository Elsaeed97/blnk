from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import CustomUser
from rest_framework.authtoken.models import Token


class UserRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("user-registration")
        self.payload = {
            "username": "testuser",
            "password": "testpassword",
            "email": "test@example.com",
            "role": "LOAN_PROVIDER",
        }

    def test_user_registration(self):
        response = self.client.post(self.url, data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, "testuser")

class CustomAuthTokenTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("login")
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.payload = {
            "username": "testuser",
            "password": "testpassword",
        }

    def test_custom_auth_token(self):
        response = self.client.post(self.url, data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("token" in response.data)
        self.assertTrue(Token.objects.filter(user=self.user).exists())

    def test_invalid_credentials(self):
        payload = {
            "username": "testuser",
            "password": "wrongpassword",
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue("error" in response.data)

