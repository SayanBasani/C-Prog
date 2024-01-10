# from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('a/',include('sayanst.urls')),
    path('b/',include('app.url')),
]
