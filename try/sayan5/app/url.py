from django.urls import path,include
from app import views

urlpatterns = [
    path("HOME/",views.home),
    path("info/",views.i),
    path('page/',views.p),
    # path('',views.tr),
    path('',views.sinin),
]