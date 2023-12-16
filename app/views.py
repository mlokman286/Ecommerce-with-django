from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate,login,logout
from .forms import UserCreateForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request,new_user)
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request,'registration/signup.html',{'form':form})
# def Master(request):
#     return render(request,'master.html')
def Index(request):
    catagory = Catagory.objects.all()
    catagoryID = request.GET.get('category')
    brands = Brand.objects.all()
    brandID = request.GET.get('brand')
    if catagoryID:
        products = Product.objects.filter(sub_catagory = catagoryID).order_by('-id')
    elif brandID:
        products = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        products = Product.objects.all().order_by('-id')
    context = {
        'catagory':catagory,
        'products':products,
        'brands':brands,
    }
    return render(request,'index.html',context)

@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def contact_page(request):
    if request.method == "POST":
        contact = ContacUs(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']
        )
        contact.save()
    return render(request, 'contact.html')

def checkout(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)

        for i in cart:
            a = int(cart[i]['price'])
            b = int(cart[i]['quantity'])
            total = a*b

            order = Order(
            user = user,
            product=cart[i]['name'],
            price = cart[i]['price'],
            quantity = cart[i]['quantity'],
            image = cart[i]['image'],
            address = address,
            phone = phone,
            pincode = pincode,
            total = total
            )
            order.save()
        request.session['cart']={}
        return redirect('home')  

def user_order(request):
    user = request.user
    order =  Order.objects.filter(user=user)
    context = {
        'order':order
    }
    return render(request,'order.html',context)


def product(request):
    catagory = Catagory.objects.all()
    catagoryID = request.GET.get('category')
    brands = Brand.objects.all()
    brandID = request.GET.get('brand')
    if catagoryID:
        products = Product.objects.filter(sub_catagory = catagoryID).order_by('-id')
    elif brandID:
        products = Product.objects.filter(brand = brandID).order_by('-id')
    else:
        products = Product.objects.all().order_by('-id')
    context = {
        'catagory':catagory,
        'products':products,
        'brands':brands,
    }
    return render(request,'product.html',context)

def product_detail(request,id):
    product = Product.objects.filter(id = id).first()
    context = {
        'product':product,
    }
    return render(request, 'product_detail.html',context)

def search(request):
    query = request.GET['search']
    product = Product.objects.filter(name__icontains = query)
    context = {
        'product':product,
    }
    return render(request,'search.html',context)

