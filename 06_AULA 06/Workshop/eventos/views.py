from django.shortcuts import render
from .forms import EventoForm

def cadastrar_evento(request):
    dados = None
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            dados = form.cleaned_data
    else:
        form = EventoForm()

    return render(request, 'eventos/cadastro.html', {'form': form, 'dados': dados})