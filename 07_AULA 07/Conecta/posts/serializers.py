from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comentario, Hashtag, Notificacao

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'