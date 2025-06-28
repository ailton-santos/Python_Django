from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # URLs para livros
    path('livros/', views.lista_livros, name='lista_livros'),
    path('livros/<int:pk>/', views.detalhe_livro, name='detalhe_livro'),
    path('livros/novo/', views.criar_livro, name='criar_livro'),
    
    # URLs para usuários
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/<int:pk>/', views.detalhe_usuario, name='detalhe_usuario'),
    path('usuarios/novo/', views.criar_usuario, name='criar_usuario'),
    
    # URLs para empréstimos
    path('emprestimos/', views.lista_emprestimos, name='lista_emprestimos'),
    path('emprestimos/novo/', views.criar_emprestimo, name='criar_emprestimo'),
    path('emprestimos/<int:pk>/devolver/', views.devolver_livro, name='devolver_livro'),
]