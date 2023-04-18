from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
     path('home/', views.home, name='home'),
     path('', views.home, name='home'),
     path('collection/',views.collection,name='collection'),
     path('contactus/',views.contact_us, name='contactus'),
     path('aboutus/',views.about_us, name='aboutus'),
     path('login',views.login_view, name='login'),
     path('signup/',views.signup_view, name='signup'),
     path('signout/',views.signout_view , name='signout'),
     path('products/<int:pk>/', views.productdetail, name='productdetail'),
     path('category/<int:pk>/', views.category_view, name='category_view'),
     path('category_sort_in/<int:pk>/', views.sort_increment_product, name='category_sort_in'),
     path('category_sort_de/<int:pk>/', views.sort_decrement_product, name='category_sort_de'),
     path('profile/',views.profile_view, name='profile'),

     path('update_profile_user/', views.update_profile_user, name='update_profile_user'),
     path('changepassword_view/', views.change_password_view, name='changepassword_view'),
     path('update_pass_user/', views.update_password_user, name='update_password_user'),

     path('add_to_cart', views.add_to_cart, name='add_to_cart'),
     path('cart/', views.cart, name='cart'),
     path('checkout/', views.payment_view, name='checkout'),
     path('order/', views.order, name='order'),


     path('increment_product',views.increment_product, name='increment_product'),
     path('decrement_product',views.decrement_product, name='decrement_product'),
     
     path('search_product/',views.search_product, name='search_product'),
     path('review/',views.Review_Rate, name='reivew'),
     path('remove_product/<int:pk>/',views.remove_product, name='remove_product'),
     path('plus_cart/<int:pk>/', views.plus_item, name='plus_cart'),
     path('minus_cart/<int:pk>/', views.minus_item, name='minus_cart'),


     path('adminlogin/',views.admin_login_view, name='adminlogin'),
     path('loginadmin/',views.admin_login, name='loginadmin'),
     path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
     path('logoutadmin/',views.logout_view, name='logoutadmin'),
     path('customer_view/',views.customer_view, name='customer_view'),
     path('product_view/',views.product_view, name='product_view'),
     path('customer_update_view/<int:pk>',views.customer_update_view, name='customer_update_view'),
     path('update_customer/',views.update_customer, name='update_customer'),
     path('delete_customer/<int:pk>', views.delete_customer, name='delete_customer'),

     path('category_view_admin/',views.category_view_admin, name='category_view_admin'),
     path('add_category_view/', views.add_category_view, name='add_category_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)