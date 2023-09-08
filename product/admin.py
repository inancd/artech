from django.contrib import admin
from .models import (Product, ProductCategory, ProductImage)
from mptt.admin import MPTTModelAdmin

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('name', )}
    inlines = [ProductImageInline]
    


class ProductCategoryAdmin(MPTTModelAdmin):
    prepopulated_fields= {'slug': ('name', )}

admin.site.register(ProductCategory, ProductCategoryAdmin)



