from dataclasses import fields
from importlib import import_module
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.db import models

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Profile(ModelForm):
    profile_picure = forms.ImageField(label=('Update Profile'),required=False, \
                                    error_messages ={'invalid':("Image files only")},\
                                    widget=forms.FileInput)
    class Meta:
        model = Customer
        fields = '__all__'
        exclude= ['user']

class Product(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        exclude= ['user']

class order(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        exclude = ['item','seller','status']

class Updateorder(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        exclude = ['item','seller','qty']


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)

