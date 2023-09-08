from django.urls import path
from product import views

app_name= 'product'

urlpatterns = [
    path("", views.productAll, name='product'),
    path('menu/', views.category, name='menu'),
    path('<slug:slug>/', views.productDetail, name='product_detail'),
    path('<slug:category_slug>', views.productList, name='product_list'),
    
    
]