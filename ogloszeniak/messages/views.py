from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def my_messages(request):
    template = loader.get_template('messages_main.html')
    context = {
        'power': 'power'
    }

    return HttpResponse(template.render(context,request))