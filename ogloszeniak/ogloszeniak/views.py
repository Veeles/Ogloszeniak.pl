from django.template import loader
from django.http import HttpResponse
from listings.models import Category

def home_view(request):
    template =  loader.get_template('index.html')
    my_data = Category.objects.all().values()
    context = {
        'data':my_data,
        }
    return HttpResponse(template.render(context, request))

