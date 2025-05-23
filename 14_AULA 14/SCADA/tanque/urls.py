from django.urls import path
from . import views

urlpatterns = [
    path('', views.interface, name='ihm'),
    path('ligar/', views.ligar, name='ligar'),
    path('desligar/', views.desligar, name='desligar'),
    path('nivel/', views.estado_nivel, name='nivel'),
]
