# formulario/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.enviar_info, name='enviar_info'),
]