from django.contrib import admin
from django.urls import path,include
from sayanst import views

urlpatterns = [
    # path("",views.index,name='Home'),
    # path("about/",views.about),
    path('page/',views.page),
]
