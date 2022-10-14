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
