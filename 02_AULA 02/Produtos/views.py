from django.shortcuts import render
from .forms import ProdutoForm

def cadastrar_produto(request):
    mensagem = ''
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            mensagem = f"Produto '{dados['nome']}' cadastrado com sucesso!"
    else:
        form = ProdutoForm()

    return render(request, 'produtos/cadastro.html', {'form': form, 'mensagem': mensagem})
