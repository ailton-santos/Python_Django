from django.shortcuts import render
from .forms import CursoForm

def cadastrar_curso(request):
    dados = None
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
    else:
        form = CursoForm()

    return render(request, 'cursos/cadastro.html', {'form': form, 'dados': dados})
