from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    phone= models.CharField(max_length=100,null=True)
    profile_picure = models.ImageField(null=True,blank=True,error_messages = {'invalid':("Image files only")})
    creator = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=10000,null=False,default='0')
    tags = models.CharField(max_length=100,null=True)
    Image = models.ImageField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name

class Orders(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out For Delivary','Out For Delivary'),
        ('Delivered','Delivered')
    )
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    seller =  models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='Seller')
    item = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    qty = models.CharField(max_length=190)
    status = models.CharField(max_length=190,choices=STATUS,default='Pending')
    date_ordered = models.DateTimeField(auto_now_add=True)
    
   


class OrderItems(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    qty = models.IntegerField()
    ordered = models.BooleanField(default=False)
    # coupon = models.ForeignKey(
    #     'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    # billing_address = models.ForeignKey(
    #     'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item)

    def price(self):
        return int(self.qty) * int(self.item.price)
    
    def get_total(self):
        x = 0
        for i in self.item.all():
            x+= int(i.price())
        if self.coupon:
            x -= self.coupon.amount
        return x

class Address(models.Model):
    
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code
