from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_produto, name='cadastrar_produto'),
]