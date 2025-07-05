from django.contrib import admin
from .models import Autor, Categoria, Livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nacionalidade', 'data_nascimento']
    search_fields = ['nome', 'nacionalidade']
    list_filter = ['nacionalidade']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    search_fields = ['nome']

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'ano_publicacao', 'disponivel']
    list_filter = ['disponivel', 'categoria', 'ano_publicacao']
    search_fields = ['titulo', 'autor__nome', 'isbn']
    list_editable = ['disponivel']
    date_hierarchy = 'data_cadastro'