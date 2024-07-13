from django.test import TestCase, Client
from .serializer import PasswordSerializer
from django.urls import reverse


# testing the serializer
class TestSerializer(TestCase):

    def test_PasswordSerializer(self):
        data = {
            "password_length": 12,
            "uppercase": True,
            "numbers": True,
            "symbols": False,
        }

        serializer = PasswordSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        validated_data = serializer.validated_data

        self.assertEqual(validated_data["password_length"], 12)
        self.assertTrue(validated_data["uppercase"])
        self.assertTrue(validated_data["numbers"])
        self.assertFalse(validated_data["symbols"])


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        # storing the urls
        self.password_url = reverse("password:Password_Generator")

    def test_PasswordGenerator_POST(self):
        data = {
            "password_length": 12,
            "uppercase": True,
            "numbers": True,
            "symbols": False,
        }
        response = self.client.post(self.password_url, data, format="json")
        self.assertEqual(response.status_code, 200)
