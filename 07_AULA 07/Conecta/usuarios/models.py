from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
import os

class Usuario(AbstractUser):
    """NOVO: Custom User Model estendido"""
    
    TIPO_CONTA_CHOICES = [
        ('pessoal', 'Pessoal'),
        ('business', 'Business'),
        ('creator', 'Creator'),
    ]
    
    # Campos adicionais
    bio = models.TextField(max_length=500, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=50, blank=True)
    pais = models.CharField(max_length=50, default='Brasil')
    
    # Imagens
    foto_perfil = models.ImageField(upload_to='perfis/', blank=True, null=True)
    foto_capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    
    # Configurações da conta
    tipo_conta = models.CharField(max_length=20, choices=TIPO_CONTA_CHOICES, default='pessoal')
    conta_verificada = models.BooleanField(default=False)
    conta_privada = models.BooleanField(default=False)
    
    # Timestamps
    ultima_atividade = models.DateTimeField(auto_now=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # Estatísticas (cache)
    total_posts = models.PositiveIntegerField(default=0)
    total_seguidores = models.PositiveIntegerField(default=0)
    total_seguindo = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"@{self.username}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # NOVO: Redimensionar imagem de perfil automaticamente
        if self.foto_perfil:
            img = Image.open(self.foto_perfil.path)
            if img.height > 300 or img.width > 300:
                img.thumbnail((300, 300))
                img.save(self.foto_perfil.path)
    
    def get_nome_completo(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username
    
    def get_foto_perfil_url(self):
        if self.foto_perfil:
            return self.foto_perfil.url
        return '/static/images/default-avatar.png'

class Seguidor(models.Model):
    """NOVO: Sistema de seguidores many-to-many customizado"""
    seguidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguindo_set')
    seguido = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguidores_set')
    data_inicio = models.DateTimeField(auto_now_add=True)
    notificacoes_ativas = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['seguidor', 'seguido']
        verbose_name = 'Relacionamento de Seguidor'
        verbose_name_plural = 'Relacionamentos de Seguidores'
    
    def __str__(self):
        return f"{self.seguidor.username} segue {self.seguido.username}"