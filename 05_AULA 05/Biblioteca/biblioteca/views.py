from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # NOVO CONCEITO!
from django.db.models import Q  # Para filtros avançados
from .models import Livro, Usuario, Emprestimo, Autor, Categoria
from .forms import LivroForm, UsuarioForm, EmprestimoForm, AutorForm, CategoriaForm
from datetime import date

# View principal
def home(request):
    total_livros = Livro.objects.count()
    livros_disponiveis = Livro.objects.filter(status='disponivel').count()
    total_usuarios = Usuario.objects.filter(ativo=True).count()
    emprestimos_ativos = Emprestimo.objects.filter(data_devolucao__isnull=True).count()
    
    # Livros em atraso - NOVO CONCEITO: filtro avançado!
    emprestimos_atraso = Emprestimo.objects.filter(
        data_devolucao__isnull=True,
        data_prevista_devolucao__lt=date.today()
    )
    
    context = {
        'total_livros': total_livros,
        'livros_disponiveis': livros_disponiveis,
        'total_usuarios': total_usuarios,
        'emprestimos_ativos': emprestimos_ativos,
        'emprestimos_atraso': emprestimos_atraso.count(),
    }
    return render(request, 'biblioteca/home.html', context)

# Views para Livros
def lista_livros(request):
    # Filtro por busca - NOVO CONCEITO!
    busca = request.GET.get('busca')
    status_filtro = request.GET.get('status')
    
    livros = Livro.objects.all().order_by('titulo')
    
    if busca:
        livros = livros.filter(
            Q(titulo__icontains=busca) | 
            Q(autor__nome__icontains=busca) | 
            Q(isbn__icontains=busca)
        )
    
    if status_filtro:
        livros = livros.filter(status=status_filtro)
    
    return render(request, 'biblioteca/lista_livros.html', {'livros': livros, 'busca': busca, 'status_filtro': status_filtro})

def detalhe_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    emprestimos = livro.emprestimos.all().order_by('-data_emprestimo')[:5]  # Últimos 5
    return render(request, 'biblioteca/detalhe_livro.html', {'livro': livro, 'emprestimos': emprestimos})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')  # NOVO CONCEITO!
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/criar_livro.html', {'form': form})

# Views para Usuários
def lista_usuarios(request):
    usuarios = Usuario.objects.filter(ativo=True).order_by('nome')
    return render(request, 'biblioteca/lista_usuarios.html', {'usuarios': usuarios})

def detalhe_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    emprestimos_ativos = usuario.emprestimos.filter(data_devolucao__isnull=True)
    historico = usuario.emprestimos.filter(data_devolucao__isnull=False).order_by('-data_devolucao')[:10]
    return render(request, 'biblioteca/detalhe_usuario.html', {
        'usuario': usuario, 
        'emprestimos_ativos': emprestimos_ativos,
        'historico': historico
    })

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'biblioteca/criar_usuario.html', {'form': form})

# Views para Empréstimos
def lista_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(data_devolucao__isnull=True).order_by('data_prevista_devolucao')
    return render(request, 'biblioteca/lista_emprestimos.html', {'emprestimos': emprestimos})

def criar_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            try:
                emprestimo = form.save(commit=False)
                emprestimo.clean()  # Validação customizada
                emprestimo.save()
                messages.success(request, f'Empréstimo realizado com sucesso! Devolução prevista: {emprestimo.data_prevista_devolucao.strftime("%d/%m/%Y")}')
                return redirect('lista_emprestimos')
            except Exception as e:
                messages.error(request, f'Erro ao realizar empréstimo: {str(e)}')  # NOVO CONCEITO!
    else:
        form = EmprestimoForm()
    return render(request, 'biblioteca/criar_emprestimo.html', {'form': form})

def devolver_livro(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk, data_devolucao__isnull=True)
    
    if request.method == 'POST':
        from django.utils import timezone
        emprestimo.data_devolucao = timezone.now()
        emprestimo.save()  # O método save customizado vai mudar o status do livro
        messages.success(request, f'Livro "{emprestimo.livro.titulo}" devolvido com sucesso!')
        return redirect('lista_emprestimos')
    
    return render(request, 'biblioteca/devolver_livro.html', {'emprestimo': emprestimo})