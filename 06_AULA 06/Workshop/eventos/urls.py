from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_evento, name='cadastrar_evento'),
]
