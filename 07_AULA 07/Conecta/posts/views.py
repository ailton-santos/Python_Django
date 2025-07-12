from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Post, Comentario, Hashtag, Notificacao
from .serializers import PostSerializer, ComentarioSerializer, HashtagSerializer, NotificacaoSerializer

User = get_user_model()

# ViewSets BÁSICOS - sem complicação
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class HashtagViewSet(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer

# View simples para página inicial
def rede_social_home(request):
    return render(request, 'home.html', {'mensagem': 'ConectaBrasil funcionando!'})