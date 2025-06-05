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
=======
# Create your views here.
from django.shortcuts import render, redirect
from .forms import AlunoForm

# Lista global
alunos_lista = []

def cadastro(request):
    global alunos_lista
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            nota1 = form.cleaned_data['nota1']
            nota2 = form.cleaned_data['nota2']
            nota3 = form.cleaned_data['nota3']
            nota4 = form.cleaned_data['nota4']
            media = (nota1 + nota2 + nota3 + nota4) / 4
            if media >= 6:
                status = "Aprovado" 
            else:
                status = "Reprovado"
            
            aluno = {
                'nome': nome,
                'nota1': nota1,
                'nota2': nota2,
                'nota3': nota3,
                'nota4': nota4,
                'media': round(media, 2),
                'status': status
            }
            alunos_lista.append(aluno)
            return redirect('cadastro')
    else:
        form = AlunoForm()

    return render(request, 'alunos/cadastro.html', {'form': form, 'alunos': alunos_lista})
