from django.contrib import admin
from django.urls import path, include
from usuarios import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('scada/', include('scada.urls')),
    path('calorias/', include('calorias.urls')),
    path('cep/', include('cep.urls')),
]