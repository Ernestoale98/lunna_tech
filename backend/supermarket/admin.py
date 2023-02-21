from django.contrib import admin

from backend.supermarket.models import Brand, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'brand_name', 'created_at', 'updated_at')

    @admin.display()
    def brand_name(self, obj):
        return obj.brand.name
