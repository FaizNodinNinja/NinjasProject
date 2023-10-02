from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
      path('admin/', admin.site.urls),

      path('', views.HOME, name='home'),
      path('base/', views.BASE, name='base'),
      path('about/', views.About_Us, name='about'),
      path('products/', views.PRODUCT, name='products'),
      path('products/<str:id>', views.PRODUCT_DETAIL_PAGE, name='product_detail'),

      path('contact/', views.Contact_page, name='contact'),
      path('search/', views.SEARCH, name='search'),

      path('register/', views.HandleRegister, name='register'),
      path('login/', views.HandleLogin, name='login'),
      path('logout/', views.HandleLogout, name='logout'),

      # cart urls

      path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
      path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
      path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
      path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
      path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
      path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

      path('cart/checkout/', views.Check_out, name='checkout'),

      path('cart/checkout/placeorder', views.PlaceOrder, name='place_order'),

      path('success', views.success, name='success'),

      path('yourorder/', views.Your_Order, name='yourrorder'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
