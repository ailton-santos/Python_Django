from django.urls import path
from . import views

urlpatterns = [
    path('', views.painel, name='painel'),
    path('ligar/', views.iniciar),
    path('desligar/', views.parar),
    path('nivel/', views.nivel),
]