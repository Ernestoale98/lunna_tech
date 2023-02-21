from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from backend.supermarket.models import Brand, Product
from backend.supermarket.serializers import BrandSerializer, ProductSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """API to manage Brand resource"""
    queryset = Brand.objects.all().order_by('-created_at')
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    """API to manage Product resource"""
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
