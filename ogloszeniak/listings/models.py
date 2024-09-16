from django.db import models
from django.contrib.auth.models import User

  
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image_path = models.ImageField(upload_to='photos/categoriesIcons/')
    image_background_color = models.TextField()



    def __str__(self):
        return self.name

class Product(models.Model):
    VOIVODESHIP_CHOICES = [
        ('DS', 'Dolnośląskie'),
        ('KP', 'Kujawsko-Pomorskie'),
        ('LB', 'Lubelskie'),
        ('LS', 'Lubuskie'),
        ('LD', 'Łódzkie'),
        ('MA', "Małopolskie"),
        ('MZ', 'Mazowieckie'),
        ('OP', 'Opolskie'),
        ('PK', 'Podkarpackie'),
        ('PD', "Podlaskie"),
        ('PM', "Pomorskie"),
        ('SL', "Śląskie"),
        ('SK', "Świetokrzyskie"),
        ('WM', "Warmińsko-Mazurskie"),
        ('WP', "Wielkopolskie"),
        ('ZP', "Zachodniopomorskie"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listings')
    city = models.CharField(max_length=200)
    voivodeship = models.CharField(max_length=2,choices=VOIVODESHIP_CHOICES, default='DS')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title