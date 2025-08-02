from django.contrib import admin
from .models import DiasVisita, Horario, Imovei, Cidade, Imagem, Visitas

# --- CONFIGURAÇÕES BÁSICAS ---

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    verbose_name = 'Cidade'
    verbose_name_plural = 'Cidades'

@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_preview')

    def img_preview(self, obj):
        if obj.img:
            return f"<img src='{obj.img.url}' width='100' height='75' />"
        return "-"
    img_preview.short_description = "Pré-visualização"
    img_preview.allow_tags = True


@admin.register(DiasVisita)
class DiasVisitaAdmin(admin.ModelAdmin):
    list_display = ('dia',)


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('horario',)


# --- INLINE PARA IMAGENS ---

class ImagemInline(admin.TabularInline):
    model = Imovei.imagens.through
    extra = 1

# --- IMÓVEIS ---

@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = (
        'rua',
        'numero',
        'cidade',
        'valor_formatado',
        'tipo_display',
        'tipo_imovel_display',
        'quartos',
        'tamanho',
        'tipo',
    )
    list_filter = ('cidade', 'tipo', 'tipo_imovel', 'dias_visita')
    search_fields = ('rua', 'cidade__nome', 'descricao')
    list_editable = ('tipo',)
    inlines = [ImagemInline]
    filter_horizontal = ('dias_visita', 'horarios')

    def tipo_display(self, obj):
        return dict(Imovei.TIPO_NEGOCIACAO_CHOICES).get(obj.tipo)
    tipo_display.short_description = 'Tipo de Negociação'

    def tipo_imovel_display(self, obj):
        return dict(Imovei.TIPO_IMOVEL_CHOICES).get(obj.tipo_imovel)
    tipo_imovel_display.short_description = 'Tipo de Imóvel'

    def valor_formatado(self, obj):
        return f"R$ {obj.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    valor_formatado.short_description = 'Valor'


# --- VISITAS ---

@admin.register(Visitas)
class VisitasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'imovel', 'dia', 'horario', 'get_status_display')
    list_filter = ('status', 'dia')
    search_fields = ('usuario__username', 'imovel__rua')
    autocomplete_fields = ('usuario', 'imovel')

    def get_status_display(self, obj):
        return dict(Visitas.STATUS_CHOICES).get(obj.status)
    get_status_display.short_description = 'Status'
