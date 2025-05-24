from django import forms
class CEPForm(forms.Form):
    cep = forms.CharField(max_length=9, label='CEP')

# cep/views.py
import requests
from django.shortcuts import render
from .forms import CEPForm


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
                resp = requests.get(url)
                if 'erro' not in resp.json():
                    endereco = resp.json()
                else:
                    erro = 'CEP não encontrado.'
            except:
                erro = 'Erro de conexão.'
    return render(request, 'cep/consulta.html', {'form': form, 'endereco': endereco, 'erro': erro})