from django.shortcuts import render
from .forms import FilmeForm

def cadastrar_filme(request):
    dados = None
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
    else:
        form = FilmeForm()

    return render(request, 'filmes/cadastro.html', {'form': form, 'dados': dados})
