from rest_framework import serializers
from .models import Autor, Categoria, Livro

class AutorSerializer(serializers.ModelSerializer):
    quantidade_livros = serializers.SerializerMethodField()
    
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'nacionalidade', 'data_nascimento', 'biografia', 'quantidade_livros']
    
    def get_quantidade_livros(self, obj):
        return obj.livros.count()

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']

class LivroSerializer(serializers.ModelSerializer):
    autor_nome = serializers.CharField(source='autor.nome', read_only=True)
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'autor_nome', 'categoria', 'categoria_nome', 
                 'isbn', 'ano_publicacao', 'paginas', 'disponivel', 'data_cadastro']