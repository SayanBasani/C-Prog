from django.urls import path 
from . import views

app_name='Seller'
urlpatterns = [
    path('',views.HomePage,name='Seller-HomePage'),
    path('Seller_login/',views.Seller_login,name='Seller_login'),
    path('Seller_Singup/',views.Seller_Singup,name='Seller_Singup'),
]