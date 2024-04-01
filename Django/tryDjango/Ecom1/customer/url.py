from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path("user_login/",views.user_login,name='user_login'),
    path("Singup/",views.Singup,name='Singup'),
]