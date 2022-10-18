from django.shortcuts import render,redirect
from.forms import *
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import resolve_url

# Create your views here.

def home(request):
    product = Products.objects.all()
    context = {'products':product}
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

def dashboard(request,pk):
    customer = Customer.objects.get(id=pk)
    items = Products.objects.get_queryset()
    context= {'items':items}
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

def info(request,pk):
    product = Products.objects.get(id=pk)
    context= {'product':product}
    return render(request,'main/info.html',context)

def product_register(request):
    customer = User.objects.get(username=request.user)
    form = Product(instance=customer)
    if request.method == "POST":
        form = Product(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.save()

            return redirect(f'dashboard/{request.user.customer.id}')
    context= {'form':form}
    return render(request,'main/products_register.html',context)


def updateItem(request,pk):
    productitem = Products.objects.get(id=pk)
    form = Product(instance=productitem)
    context = {'form':form}
    form = Product(request.POST,request.FILES,instance=productitem)
    if form.is_valid():
        form.save()
        return redirect(f'/dashboard/{request.user.customer.id}')
    return render(request,'main/products_register.html',context)

def deleteItem(request,pk):
    productitem = Products.objects.get(id=pk)
    if request.method == 'POST':
        productitem.delete()
        return redirect(f'/dashboard/{request.user.customer.id}')
    context = {'product':productitem}
    return render(request,'main/delete_product.html',context)

def about(request):
    context = {}
    return render(request,'main/about.html',context)