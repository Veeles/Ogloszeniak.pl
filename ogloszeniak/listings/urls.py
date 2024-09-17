
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from listings.views import product_details, create_lising, products_category

urlpatterns = [
    path('product/<int:id>/',product_details, name='product_details'),
    path('create_listing/', create_lising, name='create_lising'),
    path('products/<str:name>/', products_category, name='products_category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
