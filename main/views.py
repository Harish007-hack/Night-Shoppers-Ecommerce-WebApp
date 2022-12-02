from math import prod
from django.shortcuts import render,redirect,get_object_or_404
from.forms import *
from django.contrib.auth import authenticate,login,logout
from .filters import SearchFilter
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import *
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages

# Create your views here.

def home(request):
    if 'q' in request.GET:
        q= request.GET['q']
        product =  Products.objects.filter(Q(product_name__contains=q) |
                              Q(product_name__contains=q) |
                              Q(product_name__istartswith =q) |
                              Q(product_name__istartswith = q) |
                              Q(product_name__iendswith = q)|
                              Q(tags__istartswith = q) |
                              Q(tags__contains = q) |
                              Q(tags__iendswith = q) )
    else:
        product = Products.objects.all()
    paginator = Paginator(product,8)
    page_num = request.GET.get('page',1)
    num = paginator.num_pages
    try:
        page = paginator.page((page_num))
    except EmptyPage:
        page = paginator.page(1)

    item =  Products.objects.all()

    cart_items = OrderItems.objects.count()

    context = {'products':page,'num':num,'items':item,'count':cart_items}
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
    order = request.user.orders_set.all()
    pending = order.filter(status='Pending').count()
    delivered = order.filter(status='Delivered').count()
    items = request.user.products_set.all()
    #print(request.user.products_set.all())
    context= {'items':items,'orders':order,'pending':pending,'delivered':delivered}
    return render(request,'main/dashboard_customer.html',context)

def acc_settings(request):
    customer = request.user.customer
    form = Profile(instance=customer)
    print(request.FILES)
    if request.method == "POST":
        form = Profile(request.POST,request.FILES,instance=customer)
        print(form.is_valid())
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

def Cart_order(request,pk):
    product = Products.objects.get(id=pk)
    seller = product.user
    if request.method == "POST":
        if 'addcart' in request.POST:
            form = orderSum(request.POST)
            print(request.POST)
            print(form.is_valid())
            if form.is_valid():
                x = form.save(commit=False)
                x.item = product
                x.user = request.user
                x.buyer = request.user
                x.save()
        else:
            form = order(request.POST)
            print(request.POST)
            print(form.is_valid())
            if form.is_valid():
                x = form.save(commit=False)
                x.item = product
                x.seller = seller
                x.buyer = request.user
                x.save()
    cart_items = OrderItems.objects.count()
    others = Products.objects.filter(tags=product.tags)[:4]
    print(others)
    context= {'product':product,'count':cart_items,'others':others}
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

def status_update(request,pk):
    orderitem = Orders.objects.get(id=pk)
    status = request.POST
    print(status)
    form = Updateorder(request.POST,instance=orderitem)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        return redirect(f'/dashboard/{request.user.customer.id}')
    context = {}
    return render(request,'main/status_upadate.html',context)

def deleteOrder(request,pk):
    order =  Orders.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect(f'/dashboard/{request.user.customer.id}')
    context = {'product':order}
    return render(request,'main/delete_order.html',context)


def payment(request):
    context= {}
    return render(request,'main/payment.html',context)

def summary(request):
    orders = request.user.orderitems_set.all()
    final_price = 0
    for i in orders:
        final_price += i.price()
    print(final_price)
    context= {'orders':orders,'finalprice':final_price}
    return render(request,'main/order_summary.html',context)

def update_cart(request,pk,action):
    cart = OrderItems.objects.get(id=pk)
    if action == 'increment':
        cart.qty +=1
        cart.save()
        print(cart.qty)
    else:
        cart.qty -=1
        cart.save()
        print(cart.qty)
    return redirect('order-summary')

def delete_cart_item(request,pk):
    item = OrderItems.objects.get(id=pk)
    item.delete()
    return redirect('order-summary')

def checkout(request):
    orders = request.user.orderitems_set.all()
    final_price = 0
    for i in orders:
        final_price += i.price()
    form= CheckoutForm()
    if request.method == 'POST':
        if form.is_valid():
            form = CheckoutForm(request.POST)
            

    context = {'orders':orders,'finalprice':final_price,'form':form,'couponform': CouponForm(),'DISPLAY_COUPON_FORM': True}
    return render(request,'main/checkout.html',context)


def myorders(request):
    order = request.user.orders_set.all()
    context = {'orders':order}
    return render(request,'main/orders.html',context)

def CartOrder(request):
    orders = request.user.orderitems_set.all()
    for i in orders:
        x =Orders.objects.create(buyer=i.user,seller=i.item.user,item=i.item,qty=i.qty,status='Pending')
        x.save()
        i.ordered = True    
        i.save()
    context={}  
    return redirect('home')
    

""" def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("checkout")


def addCoupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = OrderItems.objects.get(
                    user=request.user, ordered=False)
                order.coupon = get_coupon(request, code)
                order.save()
                messages.success(request, "Successfully added coupon")
                return redirect("checkout")
            except ObjectDoesNotExist:
                messages.info(request, "You do not have an active order")
                return redirect("checkout")



    return redirect('checkout') """