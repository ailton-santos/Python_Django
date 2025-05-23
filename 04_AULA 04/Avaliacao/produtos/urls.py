from django.urls import path
from . import views

urlpatterns = [
    path('', views.avaliar_produto, name='avaliar_produto'),
]
