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


     # path('sort/', views.sort_product, name='sort'),
     path('add_to_cart', views.add_to_cart, name='add_to_cart'),
     path('cart/', views.cart, name='cart'),
     
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

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)