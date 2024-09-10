from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from django.http import HttpResponse
from .forms import RegisterForm

def login_view(response):
    if response.method == 'POST':
        pass
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
