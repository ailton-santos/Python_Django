from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import Usuario, Seguidor

@admin.register(Usuario)
class UsuarioCustomAdmin(UserAdmin):
    list_display = ['username', 'email', 'get_nome_completo', 'tipo_conta', 'conta_verificada', 'total_posts', 'foto_preview']
    list_filter = ['tipo_conta', 'conta_verificada', 'conta_privada', 'data_criacao']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_editable = ['conta_verificada']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Pessoais Extras', {
            'fields': ('bio', 'data_nascimento', 'cidade', 'estado', 'pais')
        }),
        ('Imagens', {
            'fields': ('foto_perfil', 'foto_capa')
        }),
        ('Configurações da Conta', {
            'fields': ('tipo_conta', 'conta_verificada', 'conta_privada')
        }),
        ('Estatísticas', {
            'fields': ('total_posts', 'total_seguidores', 'total_seguindo'),
            'classes': ('collapse',)
        }),
    )
    
    def foto_preview(self, obj):
        if obj.foto_perfil:
            return format_html('<img src="{}" width="40" height="40" style="border-radius: 50%;" />', obj.foto_perfil.url)
        return "📷"
    foto_preview.short_description = 'Foto'

@admin.register(Seguidor)
class SeguidorAdmin(admin.ModelAdmin):
    list_display = ['seguidor', 'seguido', 'data_inicio', 'notificacoes_ativas']
    list_filter = ['data_inicio', 'notificacoes_ativas']
    search_fields = ['seguidor__username', 'seguido__username']
    raw_id_fields = ['seguidor', 'seguido']