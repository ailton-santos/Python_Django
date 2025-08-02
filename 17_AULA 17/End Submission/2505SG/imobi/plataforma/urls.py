from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('imovel/<str:id>', views.imovel, name="imovel"), #urls dinamica para vizualizar meus imoveis
    path('agendar_visitas', views.agendar_visitas, name="agendar_visitas"), #url parar agendar as visitas
    path('agendamentos', views.agendamentos, name="agendamentos"), #url para verificar o agendamento das minhas casas
    path('cancelar_agendamento/<str:id>', views.cancelar_agendamento, name="cancelar_agendamento")
]