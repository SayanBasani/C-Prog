from django.urls import path
from . import views

urlpatterns = [
    path('',views.singin),
    path('login/',views.login),
    path('suc/',views.suc),
    path('',views.home),
]