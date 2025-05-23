from django.shortcuts import render
from .forms import AulaForm

def cadastrar_aula(request):
    dados = None
    if request.method == 'POST':
        form = AulaForm(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
    else:
        form = AulaForm()

    return render(request, 'aulas/cadastro.html', {'form': form, 'dados': dados})