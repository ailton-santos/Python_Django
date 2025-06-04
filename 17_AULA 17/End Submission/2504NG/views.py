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
