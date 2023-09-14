from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class ProductCategory(MPTTModel):
    name = models.CharField(max_length=250, db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=250)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = "categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductBrand(models.Model):
    brand_name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='product_images/', default='images/default.jpg')

    def __str__(self):
        return self.brand_name
    
class Product(models.Model):
    options = (
        ('taslak', 'Taslak'),
        ('yayınla', 'Yayınla')
    )
    category = models.ForeignKey(ProductCategory, related_name='product', on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand, related_name='brand', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    stock_code = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default=timezone.now)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    detail = models.TextField(null=True)
    status = models.CharField(max_length=10, choices=options, default='taslak')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', default="images/default.jpg")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_feature = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name + " Image"

