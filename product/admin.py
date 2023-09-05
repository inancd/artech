from django.contrib import admin
from .models import Product, ProductCategory, ProductImage
from mptt.admin import MPTTModelAdmin

# Register your models here.


admin.site.register(Product)

class ProductCategoryAdmin(MPTTModelAdmin):
    prepopulated_fields= {'slug': ('name', )}

admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(ProductImage)

