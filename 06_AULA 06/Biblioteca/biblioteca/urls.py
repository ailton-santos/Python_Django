from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'autores', views.AutorViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'livros', views.LivroViewSet)

urlpatterns = [
    path('', views.biblioteca_home, name='biblioteca_home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]