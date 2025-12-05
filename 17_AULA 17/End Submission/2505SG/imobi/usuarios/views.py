from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.messages import add_message
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth #importando o modulo de autenticacao do django

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated: #tatica de segurança para nao deixar o usuario acessar a pagina de login
            return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        #Fazendo as tratativas que o usuario nao deixe espaços em branco da minha string em formulários
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Por favor Preencha todos os campos')
            return redirect('cadastro')

        user = User.objects.filter(username=username) #aqui meus usuarios tem que ser igual ao username

        if user.exists(): #redirecionando meu usuario para o cadastro paŕa nao permitir um duplo cadastro no banco de dados
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome cadastrado')
            return redirect('cadastro')
        try:
            user = User.objects.create_user(username=username, email=email) #Criando uma instancia dos meus usuarios e ja criando
            user.set_password(senha) #Criptografa senha do usuario corretamente
            user.save() #salvando meu usuario no banco de dados
            messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!')
            return redirect('logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('cadastro')
    return None


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated: #tatica de segurança para nao deixar o usuario acessar a pagina de login
            return redirect('/')
        return render(request, 'logar.html')
    elif request.method == "POST": #caso contrario eu faço a captura do email e senha do usuario
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha) #autenticando o usuario pelo email e senha
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Error! Usuário ou senha inválidos')
            return redirect('logar')
        else:
            auth.login(request, usuario)
            return redirect('/')
    return None

def sair(request):
    auth.logout(request) #funcao para deslogar o usuario do sistema usando o django.contrib import auth do django
    return redirect('logar')

