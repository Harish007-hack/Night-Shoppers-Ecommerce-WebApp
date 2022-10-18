from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    phone= models.CharField(max_length=100,null=True)
    profile_picure = models.ImageField(null=True,blank=True)
    creator = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=10000,null=False,default='0')
    Image = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name

