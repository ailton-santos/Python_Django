from django.shortcuts import render
from .models import Livro

def lista_livros(request):
    termo = request.GET.get('termo', '')
    livros = Livro.objects.all()

    if termo:
        livros = livros.filter(
            titulo__icontains=termo
        ) | livros.filter(
            autor__icontains=termo
        )

    return render(request, 'livros/lista_livros.html', {
        'livros': livros,
        'termo': termo
    })