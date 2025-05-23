from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_curso, name='cadastrar_curso'),
]
