from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.urls import path

def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'work/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'work/detail.html',
                             {'product': product})