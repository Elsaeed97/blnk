from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import CustomUser


class UserRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("user-registration")
        self.payload = {
            "username": "testuser",
            "password": "testpass123",
            "email": "test@example.com",
            "role": "LOAN_PROVIDER",
        }

    def test_user_registration_url(self):
        url = reverse("user-registration")
        response = self.client.post(url, data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CustomAuthTokenTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("login")
        self.user = CustomUser.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.payload = {
            "username": "testuser",
            "password": "testpass123",
        }

    def test_custom_auth_token_url(self):
        url = reverse("login")
        response = self.client.post(url, data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_credentials_url(self):
        url = reverse("login")
        payload = {
            "username": "testuser",
            "password": "wrongpassword",
        }
        response = self.client.post(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
