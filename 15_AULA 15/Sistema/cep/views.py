# cep/views.py

from django.shortcuts import render
from .forms import CEPForm
import requests

def buscar_cep(request):
    endereco = None
    erro = None
    form = CEPForm()
    if request.method == 'POST':
        form = CEPForm(request.POST)
        if form.is_valid():
            cep = form.cleaned_data['cep'].replace('-', '')
            url = f'https://viacep.com.br/ws/{cep}/json/'
            try:
                response = requests.get(url)
                data = response.json()
                if 'erro' in data:
                    erro = 'CEP não encontrado.'
                else:
                    endereco = data
            except:
                erro = 'Erro de conexão com a API.'
    return render(request, 'cep/consulta.html', {
        'form': form,
        'endereco': endereco,
        'erro': erro
    })
