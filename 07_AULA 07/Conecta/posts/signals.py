from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Post, Like, Comentario, Notificacao
from usuarios.models import Seguidor

User = get_user_model()

@receiver(post_save, sender=Like)
def criar_notificacao_like(sender, instance, created, **kwargs):
    """NOVO: Cria notificação quando alguém curte um post"""
    if created and instance.usuario != instance.post.usuario:
        Notificacao.objects.create(
            usuario=instance.post.usuario,
            remetente=instance.usuario,
            tipo='like',
            post=instance.post,
            mensagem=f"{instance.usuario.get_nome_completo()} curtiu seu post"
        )

@receiver(post_save, sender=Comentario)
def criar_notificacao_comentario(sender, instance, created, **kwargs):
    """NOVO: Cria notificação para novos comentários"""
    if created and instance.usuario != instance.post.usuario:
        Notificacao.objects.create(
            usuario=instance.post.usuario,
            remetente=instance.usuario,
            tipo='comentario',
            post=instance.post,
            comentario=instance,
            mensagem=f"{instance.usuario.get_nome_completo()} comentou em seu post"
        )

@receiver(post_save, sender=Seguidor)
def criar_notificacao_seguidor(sender, instance, created, **kwargs):
    """NOVO: Notifica quando alguém segue você"""
    if created:
        Notificacao.objects.create(
            usuario=instance.seguido,
            remetente=instance.seguidor,
            tipo='seguidor',
            mensagem=f"{instance.seguidor.get_nome_completo()} começou a seguir você"
        )

@receiver(post_save, sender=Like)
def atualizar_contador_likes(sender, instance, created, **kwargs):
    """NOVO: Atualiza contador de likes no post"""
    if created:
        Post.objects.filter(pk=instance.post.pk).update(
            total_likes=models.F('total_likes') + 1
        )

@receiver(post_delete, sender=Like)
def decrementar_contador_likes(sender, instance, **kwargs):
    """NOVO: Decrementa contador quando like é removido"""
    Post.objects.filter(pk=instance.post.pk).update(
        total_likes=models.F('total_likes') - 1
    )

@receiver(post_save, sender=Comentario)
def atualizar_contador_comentarios(sender, instance, created, **kwargs):
    """NOVO: Atualiza contador de comentários"""
    if created:
        Post.objects.filter(pk=instance.post.pk).update(
            total_comentarios=models.F('total_comentarios') + 1
        )