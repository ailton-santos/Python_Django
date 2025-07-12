from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UsuarioSerializer

User = get_user_model()

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer