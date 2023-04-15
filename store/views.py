from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from forms import *
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404

# Create your views here.



def home(request):
    category = Category.objects.filter(status=0)
    product = Product.objects.filter(status=0)
    request.session['username'] = request.session.get('username')



    if request.session['username']:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

    # Lấy username của người dùng
        username = request.session['username']
        conext = {'category':category, 'product':product,'username':username,"cart": cart}
    else:
        conext = {'category':category, 'product':product,}

    return render(request, 'store/index.html',conext)

def contact_us(request):
    category = Category.objects.filter(status=0)
    product = Product.objects.filter(status=0)    
    request.session['username'] = request.session.get('username')

    if request.session['username']:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

    # Lấy username của người dùng
        username = request.session['username']
        conext = {'category':category, 'product':product,'username':username,"cart": cart}
    else:
        conext = {'category':category, 'product':product,}
    return render(request, 'store/contactus.html',conext)
def about_us(request):
    category = Category.objects.filter(status=0)    
    product = Product.objects.filter(status=0)
    request.session['username'] = request.session.get('username')

    if request.session['username']:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

    # Lấy username của người dùng
        username = request.session['username']
        conext = {'category':category, 'product':product,'username':username,"cart": cart}
    else:
        conext = {'category':category, 'product':product,}
    return render(request, 'store/aboutus.html',conext)

def collection(request):
    category = Category.objects.filter(status=0)
    product = Product.objects.filter(status=0)
    conext = {'category':category, 'product':product}


    return render(request, 'store/collection.html',{'category':category})

def productdetail(request,pk):
    category = Category.objects.filter(status=0)
    product = Product.objects.get(id = pk)
    product_review = Product.objects.get(id = pk)
    reviews = Review.objects.filter(product=product_review)    
    request.session['username'] = request.session.get('username')
    if request.session['username']:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            username = request.session['username']  
            context =   {'product': product,"cart": cart,'reviews': reviews,'username':username,'category':category}
        else:
            context = {'product': product,'reviews': reviews,'category':category}
    else:
        context = {'product': product,'reviews': reviews,'category':category}
    return render(request, 'store/product_detail.html', context)

def category_view(request, pk):
    request.session['username'] = request.session.get('username')
    category = Category.objects.all()
    category_tmp = Category.objects.get(id=pk)
    products = Product.objects.filter(category= category_tmp)
    if request.user.is_authenticated:
        if request.session['username']:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            username = request.session['username']  
            context = {'category':category, 'category_tmp':category_tmp, 'products': products, 'username':username,"cart": cart, }
        else:
            context = {'category':category, 'category_tmp':category_tmp, 'products': products,"cart": cart, }
    else:
        context = {'category':category, 'category_tmp':category_tmp, 'products': products,}

    return render(request, 'store/category.html',context)

def sort_increment_product(request, pk):
    request.session['username'] = request.session.get('username')
    category = Category.objects.all()
    category_tmp = Category.objects.get(id=pk)
    products = Product.objects.filter(category= category_tmp)
    products = products.order_by('selling_price')
    if request.user.is_authenticated:
        if request.session['username']:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            username = request.session['username']  
            context = {'category':category, 'category_tmp':category_tmp, 'products': products, 'username':username,"cart": cart, }
        else:
            context = {'category':category, 'category_tmp':category_tmp, 'products': products,"cart": cart, }
    else:
        context = {'category':category, 'category_tmp':category_tmp, 'products': products,}

    return render(request, 'store/category.html',context)

def sort_decrement_product(request, pk):
    request.session['username'] = request.session.get('username')
    category = Category.objects.all()
    category_tmp = Category.objects.get(id=pk)
    products = Product.objects.filter(category= category_tmp)
    products = products.order_by('-selling_price')
    if request.user.is_authenticated:
        if request.session['username']:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            username = request.session['username']  
            context = {'category':category, 'category_tmp':category_tmp, 'products': products, 'username':username,"cart": cart, }
        else:
            context = {'category':category, 'category_tmp':category_tmp, 'products': products,"cart": cart, }
    else:
        context = {'category':category, 'category_tmp':category_tmp, 'products': products,}

    return render(request, 'store/category.html',context)


def login_view(request):
    category = Category.objects.filter(status=0)
    product = Product.objects.filter(status=0)
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            username = request.session['username']
            messages.success(request, "Logged In Sucessfully!!")
            conext = {'category':category, 'product':product, 'username':username}
            #return render(request, 'store/index.html',conext)
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    return render(request, 'store/login.html',{'category':category})


def signup_view(request):
    category = Category.objects.filter(status=0)
    conext = {'category':category}
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('login')

    return render(request, 'store/signup.html',{'category':category})



def signout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data['id']
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        num_of_item = cart.num_of_items
        
        print(cartitem)

    return JsonResponse(num_of_item, safe=False)

def increment_product(request):
    data = json.loads(request.body)
    product_id = data['id']
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        num_of_item = cart.num_of_items
        
        print(cartitem)

    return JsonResponse(num_of_item, safe=False)


def decrement_product(request):
    data = json.loads(request.body)
    product_id = data['id']
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
        if (cartitem.quantity == 1):
            cartitem.quantity = 1
        else:
            cartitem.quantity -= 1

        cartitem.save()
        num_of_item = cart.num_of_items
        print(cartitem)

    return JsonResponse(num_of_item, safe=False)


def cart(request):
    cart =None
    cartitems = []
    request.session['username'] = request.session.get('username')
    if request.session['username']:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            cartitems = cart.cartitems.all()
            username = request.session['username']
        context = {"cart":cart, 'items':cartitems,'username':username}
    else:
        context = {"cart":cart, 'items':cartitems,}

    return render(request, 'store/cart.html',context)


def search_product(request):
    if request.method == 'POST':
       search = request.POST['search']
       product=Product.objects.filter(name__contains=search)
       conext = {'product':product}
    else:
        product = Product.objects.filter(status=0)
        conext = {'product':product}
    return render(request, 'store/search_product.html',conext)

def Review_Rate(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        comment = request.GET['comment']
        rate = request.GET['rate']
        user = request.user
        Review(user=user,product=product,comment=comment,rate=rate).save()
        return redirect('productdetail',pk=prod_id)



def remove_product(request,pk):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=pk,)
        cart = item.cart
        item.delete()
        return redirect('cart')
    else:
        return redirect('cart')

def plus_item(request,pk):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=pk)
        item.quantity += 1
        item.save()
        return redirect('cart')
    else:
        return redirect('cart')

def minus_item(request,pk):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=pk)
        if item.quantity == 1:
            item.quantity = 1
        else:
            item.quantity -= 1
        item.save()
        return redirect('cart')
    else:
        return redirect('cart')


def profile_view(request):

    return render(request, 'store/profile.html')

def admin_login_view(request):
    return render(request, 'admin/adminlogin.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']     
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)  
        if user is not None:
            if user.is_superuser:
                login(request, user)
                print("admin_dashboard")
                return redirect('admin_dashboard')
            else:
                print("adminlogin")
                return redirect('adminlogin')
    else:
        return redirect('adminlogin')
    return render(request, 'admin/adminlogin.html')
    
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    customercount= User.objects.all().count()
    productcount= Product.objects.all().count()
    context = {'customercount': customercount, 'productcount': productcount}
    return render(request, 'admin/admin_dashboard.html',context)

@login_required(login_url='adminlogin')
def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('adminlogin')


@login_required(login_url='adminlogin')
def customer_view(request):
    customers= User.objects.all()
    context = {'customers':customers}
    return render(request, 'admin/view_customer.html',context)

@login_required(login_url='adminlogin')
def product_view(request):
    products= Product.objects.all()
    context = {'products':products}
    return render(request, 'admin/view_products.html',context)

