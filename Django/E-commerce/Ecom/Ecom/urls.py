from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('HomePage.url')),
    # path('homepage/',include('HomePage.url')),
    path('customer/',include('customer.url')),
]
