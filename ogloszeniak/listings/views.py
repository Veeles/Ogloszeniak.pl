from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.http import HttpResponse
from django.template import loader
from .forms import ProductForm

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    template =  loader.get_template('product.html')
    context = {
        'product':product
    }
    return HttpResponse(template.render(context,request))

def create_lising(request, name=None):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect("/")
    template = loader.get_template('add_product.html')
    form = ProductForm()
    context = {
        "form":form
    }
    return HttpResponse(template.render(context,request))

def products_category(request, name):
    category_name = name
    category_query = get_object_or_404(Category, name=category_name)
    category_id = category_query.id
    category_objects = Product.objects.filter(category=category_id).values()
    template = loader.get_template('category.html')
    pieces = len(category_objects)
    context = {
        'products':category_objects,
        'pieces': pieces,
    }
    return HttpResponse(template.render(context,request))
# Create your views here.
