from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),      # MUDANÇA: adicionar api/ aqui
    path('api/', include('usuarios.urls')),   # MUDANÇA: adicionar api/ aqui  
    path('', include('posts.urls')),          # Para a página inicial
    path('api-auth/', include('rest_framework.urls')),
]

# Servir arquivos de media em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)