from django.contrib import admin
from django.urls import path,include
from sayanst import views
from . import views

urlpatterns = [
    # path("",views.index,name='Home'),
    # path("about/",views.about),
    # path('page/',views.page),
    # url(r'^$',views.singin())
    path('',views.singin),
    path('postsigin/',views.postsigin)
    
]
