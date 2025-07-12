from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('comentarios', views.ComentarioViewSet)
router.register('hashtags', views.HashtagViewSet)
router.register('notificacoes', views.NotificacaoViewSet)

urlpatterns = [
    path('', views.rede_social_home),
    path('', include(router.urls)),
]