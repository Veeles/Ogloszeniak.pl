from django.db import models
from listings.models import Product
from django.contrib.auth.models import User
class Thread(models.Model):
    listings = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='seller_thread', on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name='buyer_thread', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sender_message', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
# Create your models here.
