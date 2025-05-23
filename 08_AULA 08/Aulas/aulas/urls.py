from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_aula, name='cadastrar_aula'),
]
