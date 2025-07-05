from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Autor, Categoria, Livro
from .serializers import AutorSerializer, CategoriaSerializer, LivroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
    @action(detail=True, methods=['get'])
    def livros(self, request, pk=None):
        """Retorna todos os livros de um autor específico"""
        autor = self.get_object()
        livros = autor.livros.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.select_related('autor', 'categoria')
    serializer_class = LivroSerializer
    
    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        """Retorna apenas livros disponíveis"""
        livros = self.queryset.filter(disponivel=True)
        serializer = self.get_serializer(livros, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def emprestar(self, request, pk=None):
        """Marca um livro como emprestado"""
        livro = self.get_object()
        if not livro.disponivel:
            return Response(
                {'error': 'Livro já está emprestado'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        livro.disponivel = False
        livro.save()
        return Response({'message': f'Livro "{livro.titulo}" emprestado com sucesso'})

def biblioteca_home(request):
    """Página inicial com estatísticas"""
    context = {
        'total_livros': Livro.objects.count(),
        'total_autores': Autor.objects.count(),
        'livros_disponiveis': Livro.objects.filter(disponivel=True).count(),
        'livros_recentes': Livro.objects.select_related('autor')[:5]
    }
    return render(request, 'biblioteca/home.html', context)