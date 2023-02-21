from django.test import TestCase
from rest_framework import status

from backend.authentication.models import User


class TokenTestCase(TestCase):

    def setUp(self) -> None:
        User.objects.create_user(username='juan', email='ja@ja.com', password='ja.aj')

    def test_token_can_be_issued(self):
        data = {'username': 'juan', 'password': 'ja.aj'}
        response = self.client.post('/api/token/', data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.json().get('access'))
