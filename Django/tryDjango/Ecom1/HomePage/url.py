from django.urls import path
from . import views
app_name='homepage'
urlpatterns = [
    path('',views.HomePage,name='HomePage'),
    path('nav',views.nav),
    path('nav1',views.nav1),
    path('product',views.product),
]