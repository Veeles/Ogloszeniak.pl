from django.template import loader
from django.http import HttpResponse

def home_view(request):
    template =  loader.get_template('index.html')
    return HttpResponse(template.render())

