
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from listings.views import product_details, create_lising

urlpatterns = [
    path('product/<int:id>/',product_details, name='product_details'),
    path('create_listing/', create_lising, name='create_lising'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
