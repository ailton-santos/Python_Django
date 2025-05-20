# Create your views here.

# formulario/views.py
from django.shortcuts import render
from .forms import InfoForm

def enviar_info(request):
    mensagem = ''
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = f"Informação recebida: {nome} - {email}"
    else:
        form = InfoForm()

    return render(request, 'formulario/formulario.html', {'form': form, 'mensagem': mensagem})

