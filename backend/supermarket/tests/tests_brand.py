from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken
from backend.authentication.models import User
from backend.supermarket.models import Brand
from rest_framework import status
from django.db.models import ObjectDoesNotExist


class BrandTestCase(TestCase):

    def setUp(self) -> None:
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        refresh = RefreshToken.for_user(user)
        self.token = f"Bearer {refresh.access_token}"

    def test_brands_can_be_retrieved(self):
        response = self.client.get('/api/brands/', content_type='application/json',
                                   HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Brand.objects.count(), response.json().get('count'))

    def test_brand_can_be_created(self):
        data = {'name': 'Xbox'}
        response = self.client.post('/api/brands/', data, content_type='application/json',
                                    HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(Brand.objects.get(id=response.json().get('id')))

    def test_brands_can_be_deleted(self):
        brand = Brand.objects.create(name='Sony')
        response = self.client.delete(f"/api/brands/{brand.id}/", content_type='application/json',
                                      HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(ObjectDoesNotExist, lambda: Brand.objects.get(id=brand.id))

    def test_brand_can_be_retrieved(self):
        brand = Brand.objects.create(name='Samsung')
        response = self.client.get(f"/api/brands/{brand.id}/", content_type='application/json',
                                   HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Brand.objects.get(id=response.json().get('id')))

    def test_brand_can_be_updated(self):
        brand = Brand.objects.create(name='Microsoft')
        data = {'name': 'Google'}
        response = self.client.put(f"/api/brands/{brand.id}/", data, content_type='application/json',
                                   HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Brand.objects.get(id=response.json().get('id')))
