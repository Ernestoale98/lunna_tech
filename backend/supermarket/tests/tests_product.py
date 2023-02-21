from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

from backend.authentication.models import User
from backend.supermarket.models import Product, Brand
from rest_framework import status
from django.db.models import ObjectDoesNotExist


class ProductTestCase(TestCase):

    def setUp(self) -> None:
        self.brand = Brand.objects.create(name='Apple')
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        refresh = RefreshToken.for_user(user)
        self.token = f"Bearer {refresh.access_token}"

    def test_products_can_be_retrieved(self):
        response = self.client.get('/api/products/', content_type='application/json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), response.json().get('count'))

    def test_product_can_be_created(self):
        data = {
            'name': 'Iphone',
            'sku': 'IP123',
            'price': 10000.99,
            'brand': self.brand.id
        }
        response = self.client.post('/api/products/', data, content_type='application/json',
                                    HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(Product.objects.get(id=response.json().get('id')))

    def test_products_can_be_deleted(self):
        product = Product.objects.create(**{
            'name': 'Tablet',
            'sku': 'TP123',
            'price': 5000.99,
            'brand': self.brand
        })
        response = self.client.delete(f"/api/products/{product.id}/", content_type='application/json',
                                      HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(ObjectDoesNotExist, lambda: Product.objects.get(id=product.id))

    def test_product_can_be_retrieved(self):
        product = Product.objects.create(**{
            'name': 'Smartwatch',
            'sku': 'SMW123',
            'price': 6999.99,
            'brand': self.brand
        })
        response = self.client.get(f"/api/products/{product.id}/", content_type='application/json',
                                   HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Product.objects.get(id=response.json().get('id')))

    def test_product_can_be_updated(self):
        product = Product.objects.create(**{
            'name': 'AirPods',
            'sku': 'AIR123',
            'price': 4999.99,
            'brand': self.brand
        })
        data = {
            'name': 'AirPods PRO',
            'sku': 'IPP123',
            'price': 6999.99,
            'brand': self.brand.id
        }
        response = self.client.put(f"/api/products/{product.id}/", data, content_type='application/json',
                                   HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Product.objects.get(id=response.json().get('id')))
