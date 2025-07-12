from django.contrib import admin
from django.utils.html import format_html
from .models import Post, MidiaPost, Like, Comentario, Hashtag, Notificacao

class MidiaPostInline(admin.TabularInline):
    model = MidiaPost
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'tipo', 'texto_preview', 'total_likes', 'total_comentarios', 'data_criacao']
    list_filter = ['tipo', 'visivel_para', 'data_criacao']
    search_fields = ['texto', 'usuario__username']
    raw_id_fields = ['usuario']
    inlines = [MidiaPostInline]
    date_hierarchy = 'data_criacao'
    
    def texto_preview(self, obj):
        return obj.texto[:50] + '...' if len(obj.texto) > 50 else obj.texto
    texto_preview.short_description = 'Texto'

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ['nome', 'total_posts', 'trending', 'data_criacao']
    list_filter = ['trending', 'data_criacao']
    search_fields = ['nome']
    list_editable = ['trending']

@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'remetente', 'tipo', 'mensagem', 'lida', 'data_criacao']
    list_filter = ['tipo', 'lida', 'data_criacao']
    search_fields = ['usuario__username', 'remetente__username', 'mensagem']
    list_editable = ['lida']