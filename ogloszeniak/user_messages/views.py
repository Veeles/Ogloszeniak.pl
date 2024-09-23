from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Message, Thread

# Create your views here.
def my_messages(request, id):
    template = loader.get_template('messages_main.html')
    current_user = request.user
    messages = Message.objects.filter(sender = '1')
    threads = Thread.objects.filter(buyer="2")
    print(messages)
    context = {
        'threads':threads,
    }

    if id != None:
        
        print(current_user.id)


    return HttpResponse(template.render(context,request))