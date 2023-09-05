from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
# Create your views here.


def productAll(request):
    pass

def productDetail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = ProductCategory.objects.filter(parent=None)
    
    return render(request, 'product/product_detail.html', {'product': product, 'categories': categories})


def category(request):
    categories = ProductCategory.objects.filter(parent=None)
    return render(request, 'menu.html', {'categories': categories})


def productList(request, category_slug):
    def get_breadcrumb(category):
        breadcrumb = []
        while category:
            breadcrumb.insert(0, category)
            category = category.parent
        return breadcrumb
    
    category = get_object_or_404(ProductCategory, slug=category_slug)
    subcategories = category.get_descendants(include_self=True)
    categories = ProductCategory.objects.filter(parent=None)
    breadcrumb = get_breadcrumb(category)
    articles = Product.objects.filter(category__in=subcategories)

    context = {
        'category': category,
        'articles': articles,
        'categories': categories,
        'breadcrumb': breadcrumb
    }

    return render(request, 'product/product_list.html', context)

