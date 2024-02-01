from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_seller = models.BooleanField(default=False)
  is_buyer = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)  
  email = models.EmailField(default='levan@gmail.com', max_length=254)

class Seller(models.Model):
    seller = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.seller.username

class Buyer(models.Model):
    buyer = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.buyer.username
    
    
    
    