from django.shortcuts import render,redirect
from.forms import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    context = {}
    return render(request,'main/index.html',context)

def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        print(request.POST)

        if user is not None:
            login(request,user)
            return redirect('home')

    context= {}
    return render(request,'main/login.html',context)

def dashboard(request):
    context= {}
    return render(request,'main/dashboard_customer.html',context)

def acc_settings(request):
    customer = request.user.customer
    form = Profile(instance=customer)
    if request.method == "POST":
        form = Profile(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('settings')
    context= {'form':form}
    return render(request,'main/account_settings.html',context)

def logout_user(request):
    logout(request)
    return redirect('home')

def Signup(request):
    form   = UserForm()
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    context= {'form':form}
    return render(request,'main/sign-up.html',context)

def info(request):
    context= {}
    return render(request,'main/info.html',context)