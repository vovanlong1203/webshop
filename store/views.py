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
import random
# Create your views here.



def home(request):
    category = Category.objects.filter(status=0)
    product = Product.objects.filter(status=0)
    product_trend = Product.objects.filter(trending=1)
    product = random.sample(list(product),20)
    request.session['username'] = request.session.get('username')
    
    if request.session['username']:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    # Lấy username của người dùng
        username = request.session['username']
        conext = {'category':category, 'product':product,'username':username,"cart": cart,"product_trend":product_trend}
    else:
        conext = {'category':category, 'product':product,"product_trend":product_trend}
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
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    return render(request, 'store/login.html',{'category':category})

def update_profile_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        fisrtname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        user = User.objects.get(username=username)
        user.first_name = fisrtname
        user.last_name =lastname
        user.email = email
        user.save()
    return redirect('profile')

def change_password_view(request):
    request.session['username'] = request.session.get('username')
    username = request.session['username']
    username = request.user.username
    cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    user = User.objects.get_or_create(username=request.user.username)
    category = Category.objects.filter(status=0)
    context = {'username': username,"cart":cart,'category':category}
    return render(request, 'store/changepassword.html',context)

from django.contrib.auth import update_session_auth_hash

def update_password_user(request):
    request.session['username'] = request.session.get('username')
    username = request.session['username']

    if request.method == 'POST':
        user = User.objects.get(username= request.user.username)
        new_pass = request.POST['new_password']
        comfirm_pass = request.POST['confirm_newpassword']
        un = user.username
        if new_pass != comfirm_pass:
            messages.error(request,"Mật khẩu không khớp")
            
            return redirect('changepassword_view')
        user.set_password(new_pass)
        user.save()
        update_session_auth_hash(request, user)

        messages.success(request,"thay đổi mật khẩu thành công")
        return redirect('changepassword_view')

    return render(request, 'store/changepassword.html')

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

def payment_view(request):
    cart =None
    cartitems = []
    category = Category.objects.filter(status=0)
    request.session['username'] = request.session.get('username')
    if request.session['username']:
        if request.user.is_authenticated:
            user = User.objects.get(id = request.user.id )
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            cartitems = cart.cartitems.all()
            username = request.session['username']
        context = {"cart":cart, 'items':cartitems,'username':username,'category':category, 'user':user}
    else:
        context = {"cart":cart, 'items':cartitems,'category':category}

    return render(request, 'store/checkout.html', context)



def place_order(request):
    if request.method == 'POST':
        neworder = Order()
        neworder.user = request.user
        neworder.first_name = request.POST['firstname']
        neworder.last_name = request.POST['lastname']
        neworder.email = request.POST['email']
        neworder.address = request.POST['address']
        neworder.phone = request.POST['phonenumber']
        neworder.zipcode = request.POST['zipcode']

        if neworder.first_name==''or neworder.last_name == ''or neworder.email == ''or neworder.address == ''or neworder.phone == '' or neworder.zipcode == '' :
            return redirect('checkout')

        neworder.save()
        # cart = get_object_or_404(Cart, user=request.user)
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        tmp = cart
        for item in cart.cartitems.all():
            order_item = OrderItem(order=neworder, product=item.product, quantity=item.quantity,price=item.product.selling_price, total_price= item.price)
            order_item.save()
            item.delete()

    messages.success(request,"thanh cong")
    return redirect('home')

def order(request):
    if request.user.is_authenticated:

        username = request.session['username']
        cart = None
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

        try:
            orders = Order.objects.filter(user=request.user)
        except Order.DoesNotExist:
            orders = None
            
        order_items = []
        items = None
        for order in orders:
            items = OrderItem.objects.filter(order=order)
            order_items.append({'order': order, 'items': items})
        
    context = {'orders': orders, 'order_items': order_items,
               'username': username, 'cart':cart}
    
    return render(request,'store/order.html',context)

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
    category = Category.objects.filter(status=0)

    request.session['username'] = request.session.get('username')
    if request.session['username']:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            cartitems = cart.cartitems.all()
            username = request.session['username']
        context = {"cart":cart, 'items':cartitems,'username':username,'category':category}
    else:
        context = {"cart":cart, 'items':cartitems,'category':category}

    return render(request, 'store/cart.html',context)


def search_product(request):
    category = Category.objects.filter(status=0)
    if request.user.is_authenticated:
        if request.method == 'POST':
            search = request.POST['search']
            product=Product.objects.filter(name__contains=search)
            username = request.user.username
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        else:
            product = Product.objects.filter(status=0)
        conext = {'product':product,'username':username,'cart':cart,'category':category}
    else:
        if request.method == 'POST':
            search = request.POST['search']
            product=Product.objects.filter(name__contains=search)
        else:
            product = Product.objects.filter(status=0)
        conext = {'product':product,'category':category}
    
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
    category = Category.objects.filter(status=0)
    request.session['username'] = request.session.get('username')
    if request.session['username']:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            cartitems = cart.cartitems.all()
            username = request.session['username']
            user = User.objects.get_or_create(username=username)
        context = {"cart":cart, 'items':cartitems,'username':username,'category':category}
    else:
        context = {'category':category}

    return render(request, 'store/profile.html',context)

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

@login_required(login_url='adminlogin')
def customer_update_view(request,pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render(request, 'admin/customer_update_view.html',context)

@login_required(login_url='adminlogin')
def update_customer(request):
    id_user = request.POST['id_user']
    fisrtname = request.POST['firstname']
    lastname = request.POST['lastname']
    username = request.POST['username']
    email = request.POST['email']
    user = User.objects.get(id=id_user)
    user.first_name = fisrtname
    user.last_name =lastname
    user.email = email
    user.username = username
    user.save()
    return redirect('customer_view')
    

@login_required(login_url='adminlogin')
def delete_customer(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('customer_view')


@login_required(login_url='adminlogin')
def category_view_admin(request):
    categorys= Category.objects.all()
    context = {'categorys':categorys}
    return render(request, 'admin/view_category.html',context)


@login_required(login_url='adminlogin')
def add_category_view(request):
    return render(request, 'admin/add_category_view.html')

@login_required(login_url='adminlogin')
def cart_view_admin(request):
    carts= Cart.objects.all()
    context = {'carts':carts}
    return render(request, 'admin/view_cart.html',context)

@login_required(login_url='adminlogin')
def cartitem_view_admin(request):
    cartitems= CartItem.objects.all()
    context = {'cartitems':cartitems}
    return render(request, 'admin/view_cartitem.html',context)

@login_required(login_url='adminlogin')
def review_view_admin(request):
    reviews= Review.objects.all()
    context = {'reviews':reviews}
    return render(request, 'admin/view_review.html',context)

@login_required(login_url='adminlogin')
def order_view_admin(request):
    orders= Order.objects.all()
    context = {'orders':orders}
    return render(request, 'admin/view_order.html',context)

@login_required(login_url='adminlogin')
def orderitem_view_admin(request):
    orderitems= OrderItem.objects.all()
    context = {'orderitems':orderitems}
    return render(request, 'admin/view_orderitem.html',context)