from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
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

def create_lising(request):
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
# Create your views here.
