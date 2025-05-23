from django.urls import path
from . import views

urlpatterns = [
    path('', views.aula_com_midia, name='aula_com_midia'),
]
