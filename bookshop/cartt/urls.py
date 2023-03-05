from django.urls import path

from cartt.views import add_to_cart, cart, checkout, hx_menu_cart, update_cart, hx_cart_total, success
from core.views import  shop
from product.views import product


urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('success/', success, name='success'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]