from django.shortcuts import render
from .forms import AvaliacaoForm

def avaliar_produto(request):
    dados = None
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
    else:
        form = AvaliacaoForm()

    return render(request, 'produtos/avaliacao.html', {'form': form, 'dados': dados})