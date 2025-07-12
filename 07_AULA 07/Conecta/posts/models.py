from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import re

User = get_user_model()

class HashtagManager(models.Manager):
    def get_or_create_from_text(self, texto):
        """NOVO: Extrai e cria hashtags automaticamente"""
        hashtags = re.findall(r'#(\w+)', texto)
        hashtag_objects = []
        for tag in hashtags:
            hashtag, created = self.get_or_create(nome=tag.lower())
            hashtag_objects.append(hashtag)
        return hashtag_objects

class Hashtag(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    total_posts = models.PositiveIntegerField(default=0)
    trending = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    objects = HashtagManager()
    
    def __str__(self):
        return f"#{self.nome}"
    
    class Meta:
        ordering = ['-total_posts', '-data_criacao']

class Post(models.Model):
    TIPO_CHOICES = [
        ('texto', 'Texto'),
        ('foto', 'Foto'),
        ('video', 'Vídeo'),
        ('link', 'Link'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='texto')
    texto = models.TextField(max_length=2000, blank=True)
    
    # Localização
    localizacao = models.CharField(max_length=200, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    # Estatísticas (cache para performance)
    total_likes = models.PositiveIntegerField(default=0)
    total_comentarios = models.PositiveIntegerField(default=0)
    total_compartilhamentos = models.PositiveIntegerField(default=0)
    
    # Configurações
    comentarios_habilitados = models.BooleanField(default=True)
    visivel_para = models.CharField(
        max_length=20,
        choices=[('publico', 'Público'), ('seguidores', 'Seguidores'), ('privado', 'Privado')],
        default='publico'
    )
    
    # Timestamps
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Relacionamentos
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    
    def save(self, *args, **kwargs):
        # NOVO: Detectar tipo do post automaticamente
        if not self.tipo:
            if self.midias.exists():
                primeira_midia = self.midias.first()
                if primeira_midia:
                    self.tipo = primeira_midia.tipo
            else:
                self.tipo = 'texto'
        
        super().save(*args, **kwargs)
        
        # NOVO: Processar hashtags automaticamente
        if self.texto:
            hashtags = Hashtag.objects.get_or_create_from_text(self.texto)
            self.hashtags.set(hashtags)
    
    def __str__(self):
        return f"Post de @{self.usuario.username} - {self.data_criacao.strftime('%d/%m/%Y')}"
    
    class Meta:
        ordering = ['-data_criacao']

class MidiaPost(models.Model):
    """NOVO: Modelo para múltiplas mídias por post"""
    TIPO_CHOICES = [
        ('foto', 'Foto'),
        ('video', 'Vídeo'),
    ]
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='midias')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    arquivo = models.FileField(upload_to='posts/%Y/%m/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    ordem = models.PositiveIntegerField(default=0)
    texto_alternativo = models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['ordem']

class Like(models.Model):
    """NOVO: Sistema de likes otimizado"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['usuario', 'post']
        indexes = [
            models.Index(fields=['post', '-data_criacao']),
        ]

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField(max_length=500)
    
    # NOVO: Comentários aninhados (replies)
    comentario_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respostas')
    
    total_likes = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    editado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-data_criacao']

class Notificacao(models.Model):
    """NOVO: Sistema de notificações"""
    TIPO_CHOICES = [
        ('like', 'Curtida'),
        ('comentario', 'Comentário'),
        ('seguidor', 'Novo Seguidor'),
        ('mencao', 'Menção'),
        ('compartilhamento', 'Compartilhamento'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificacoes')
    remetente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificacoes_enviadas')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    
    # Referências opcionais
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, null=True, blank=True)
    
    mensagem = models.CharField(max_length=200)
    lida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_criacao']
        indexes = [
            models.Index(fields=['usuario', 'lida', '-data_criacao']),
        ]