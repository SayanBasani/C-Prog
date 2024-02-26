from django.urls import path,include
from app import views

from .views import login_view, logout_view

urlpatterns = [
    # path("HOME/",views.home),
    # path("info/",views.i),
    # path('page/',views.p),
    # path('',views.tr),
    # path('',views.sinin),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]