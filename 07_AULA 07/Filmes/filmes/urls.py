from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_filme, name='cadastrar_filme'),
]