from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Profile(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude= ['user']

class Product(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        exclude= ['user']