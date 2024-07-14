# from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('sayanst.urls')),
    # path('b/',include('app.url')),
]
