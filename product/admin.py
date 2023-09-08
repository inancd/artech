from django.contrib import admin
from .models import Product, ProductCategory, ProductImage
from mptt.admin import MPTTModelAdmin

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('name', )}

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(MPTTModelAdmin):
    prepopulated_fields= {'slug': ('name', )}

admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(ProductImage)

