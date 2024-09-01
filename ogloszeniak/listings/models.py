from django.db import models

  
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image_path = models.ImageField(upload_to='photos/categoriesIcons/')
    image_background_color = models.TextField()



    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField()
    crated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listings')
    
    def __str__(self):
        return self.name