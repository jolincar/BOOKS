from django.urls import path
from django.contrib.auth import views

from core.views import frontpage, shop, signup, myaccount, edit_myaccount, add_product, edit_product, delete_product
from product.views import product


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('shop/add_product/', add_product, name='add_product'),
    path('shop/edit_product/<int:pk>/', edit_product, name='edit_product'),
    path('shop/delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/edit/', edit_myaccount, name='edit_myaccount'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
]