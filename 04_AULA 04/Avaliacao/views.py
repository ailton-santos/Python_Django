from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import InfoForm, AvaliacaoForm
from django.urls import reverse
from django.http import HttpResponse


# def enviar_info(request): #view para cadastrar produto
#     mensagem = ''
#     if request.method == 'POST':
#         form = InfoForm(request.POST)
#         if form.is_valid():
#             # aqui você pode salvar ou processar os dados se quiser
#             mensagem = "Cadastro efetuado com sucesso!"
#             return redirect('avaliacao_produto')  # redireciona para a avaliação
#     else:
#         form = InfoForm()

#     return render(request, 'formulario/formulario.html', {'form': form, 'mensagem': mensagem})


def enviar_info(request):
    mensagem = ''
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            mensagem = "Cadastro efetuado com sucesso!"
            # return redirect('avaliacao_produto')
            # return redirect('/avaliacao/')
            # return redirect(reverse('avaliacao_produto'))
            return redirect(reverse('avaliacao_produto'))
    else:
        form = InfoForm() 

    return render(request, 'formulario/formulario.html', {'form': form, 'mensagem': mensagem})


def avaliacao_produto(request): #view para avaliação de produto
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            # nota = form.cleaned_data['nota']
            comentario = form.cleaned_data['comentario']
            return render(request, 'formulario/obrigado.html', {'comentario': comentario})
    else:
        form = AvaliacaoForm()

    print("Form de avaliação:", form)
    return render(request, 'formulario/avaliacao.html', {'form': form})

# def avaliacao_produto(request):
#     return HttpResponse("O template vai carregar aqui.")