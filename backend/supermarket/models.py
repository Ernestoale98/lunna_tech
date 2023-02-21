from django.core.validators import MinValueValidator
from django.db import models


class BaseModel(models.Model):
    """Abstract BaseModel with generic fields"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Brand(BaseModel):
    """Brand Model"""
    name = models.CharField(
        max_length=30,
        unique=True,
        help_text="Required, String(30), Unique field"
    )

    def __str__(self):
        return self.name


class Product(BaseModel):
    """Product Model"""
    name = models.CharField(
        max_length=30,
        unique=True,
        help_text="Required, String(30), Unique field"
    )
    sku = models.CharField(
        max_length=30,
        unique=True,
        db_index=True,
        help_text="Required, String(60), Unique field, Index"
    )
    price = models.DecimalField(
        validators=[MinValueValidator(0.1)],
        decimal_places=2,
        max_digits=10
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        help_text="Required, Id of brand")

    def __str__(self):
        return self.name


class ProductRequestLog(BaseModel):
    """ProductRequestLog Model
    this model is used to track how many times and
    when a product is queried"""
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        help_text="Required, Id of product"
    )

    class Meta:
        db_table = "supermarket_product_request_log"
