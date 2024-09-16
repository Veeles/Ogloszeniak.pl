from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from django.http import HttpResponse
from .forms import RegisterForm
from listings.models import Product

def my_account(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    template = loader.get_template('myaccount.html')
    listings = Product.objects.filter(user = request.user).values() 
    print(listings)
    context = {
        'username':username,
        'listings': listings
    }
    return HttpResponse(template.render(context, request))

def register_view(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    template = loader.get_template('register.html')
    context = {
        'form':form
    }
    return HttpResponse(template.render(context,response))
# Create your views here.
