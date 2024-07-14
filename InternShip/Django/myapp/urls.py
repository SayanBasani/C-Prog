
from django.urls import path
from.import views


urlpatterns = [
    path('',views.home),
    path('test/',views.info),
    path('info/',views.info),
    path('game/',views.game),
    path('fom/',views.fom),

]
