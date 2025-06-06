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

from.forms import InstrumentoForm

def enviar_info(request):
    mensagem = ""
    if request.method == "POST":
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            descricao = form.cleaned_data["descricao"]
            numero_de_serie = form.cleaned_data["numero_de_serie"]
            area_de_utilizacao = form.cleaned_data["area_de_utilizacao"]
            
            return render (request, 'instrumento/sucesso.html')
            #mensagem = f"Cadastro realizado com sucesso: {nome}, {descricao}, {numero_de_serie} e {area_de_utilizacao}"
        
    else:
        form = InstrumentoForm()
    
    return render(request, 'instrumento/instrumento.html', {'form':form, 'mensagem': mensagem})
