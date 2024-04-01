from django.urls import path , include

from . import views
app_name='Seller'
urlpatterns = [
    path('',views.HomePage,name='Seller-HomePage'),
]