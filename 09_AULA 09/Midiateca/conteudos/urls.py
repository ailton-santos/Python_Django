from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_conteudo, name='cadastrar_conteudo'),
]
