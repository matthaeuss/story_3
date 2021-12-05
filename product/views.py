from django.shortcuts import render
from product.models import Product

def product(request, pk):
    item = Product.objects.get(pk=pk)
    return render(request, 'product/product.html', {'product': item})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})
