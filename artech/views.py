from django.shortcuts import render

from product.models import ProductCategory


def homePage(request):
    categories = ProductCategory.objects.filter(parent=None)
    return render(request, 'index.html', {'categories': categories})

