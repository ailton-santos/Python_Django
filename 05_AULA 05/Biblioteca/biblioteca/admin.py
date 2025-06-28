from django.contrib import admin
from .models import Autor, Categoria, Livro, Usuario, Emprestimo

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento')
    search_fields = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'status', 'ano_publicacao')
    list_filter = ('status', 'categoria', 'ano_publicacao')
    search_fields = ('titulo', 'autor__nome', 'isbn')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'ativo', 'data_cadastro')
    list_filter = ('ativo', 'data_cadastro')
    search_fields = ('nome', 'email')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_emprestimo', 'data_prevista_devolucao', 'data_devolucao')
    list_filter = ('data_emprestimo', 'data_prevista_devolucao')
    search_fields = ('livro__titulo', 'usuario__nome')