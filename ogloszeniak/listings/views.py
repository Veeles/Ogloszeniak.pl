from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
from django.template import loader

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    template =  loader.get_template('product.html')
    print(product.photo.path)  # Pełna ścieżka do pliku
    print(product.photo.url)  # URL obrazu
    context = {
        'product':product
    }
    return HttpResponse(template.render(context,request))
# Create your views here.
