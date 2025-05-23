import requests
from django.shortcuts import render
from .forms import CEPForm

def buscar_cep(request):
    dados = None
    erro = None

    if request.method == 'POST':
        form = CEPForm(request.POST)
        if form.is_valid():
            cep_input = form.cleaned_data['cep'].replace('-', '').strip()
            url = f'https://viacep.com.br/ws/{cep_input}/json/'
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    resultado = response.json()
                    if 'erro' not in resultado:
                        dados = resultado
                    else:
                        erro = 'CEP não encontrado.'
                else:
                    erro = 'Erro ao acessar a API.'
            except:
                erro = 'Erro de conexão com a API.'
    else:
        form = CEPForm()

    return render(request, 'cep/busca.html', {'form': form, 'dados': dados, 'erro': erro})
