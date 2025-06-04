from django.shortcuts import render
from .forms import InfoForm

def enviar_info(request): #request confirma se o formulario esta sendo enviado
    mensagem = ''

    if request.method == 'POST':  #POST
        form = InfoForm(request.POST)
        if form.is_valid():
            nomeProduto = form.cleaned_data['nomeProduto']
            descricao = form.cleaned_data['descricao']
            preco = form.cleaned_data['preco']
            quantidadeEstoque = form.cleaned_data['quantidadeEstoque']
            categoria = form.cleaned_data['categoria']
            mensagem = f"Cadastro efetuado com sucesso!"
    else:
        form = InfoForm() #coloquei os parenteses, se der erro tira q tava certo antes
    return render (request, 'formulario/formulario.html', {'form' : form, 'mensagem' : mensagem})


