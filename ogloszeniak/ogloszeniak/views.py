from django.template import loader
from django.http import HttpResponse
from listings.models import Category, Product

def home_view(request):
    template =  loader.get_template('index.html')
    categories = Category.objects.all().values()
    products = Product.objects.order_by('-created_at')
    context = {
        'categories':categories,
        'products':products
        }
    return HttpResponse(template.render(context, request))

