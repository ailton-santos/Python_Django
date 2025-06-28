from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, timedelta

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField(blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Autores"

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    # Choices para status do livro - NOVO CONCEITO!
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
        ('reservado', 'Reservado'),
        ('manutencao', 'Em Manutenção'),
    ]
    
    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacao = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor.nome}"
    
    # Método personalizado - NOVO CONCEITO!
    def pode_ser_emprestado(self):
        """Verifica se o livro está disponível para empréstimo"""
        return self.status == 'disponivel'
    
    # Property para cor do status - NOVO CONCEITO!
    @property
    def cor_status(self):
        cores = {
            'disponivel': 'green',
            'emprestado': 'red',
            'reservado': 'orange',
            'manutencao': 'gray'
        }
        return cores.get(self.status, 'black')

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
    # Método personalizado
    def pode_pegar_emprestado(self):
        """Verifica se o usuário não tem empréstimos em atraso"""
        emprestimos_ativos = self.emprestimos.filter(data_devolucao__isnull=True)
        for emprestimo in emprestimos_ativos:
            if emprestimo.esta_em_atraso():
                return False
        return emprestimos_ativos.count() < 3  # Máximo 3 livros por vez

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_prevista_devolucao = models.DateField()
    data_devolucao = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.nome}"
    
    # Método para calcular se está em atraso - NOVO CONCEITO!
    def esta_em_atraso(self):
        if self.data_devolucao:  # Já foi devolvido
            return False
        return date.today() > self.data_prevista_devolucao
    
    # Property para dias de atraso
    @property
    def dias_atraso(self):
        if not self.esta_em_atraso():
            return 0
        return (date.today() - self.data_prevista_devolucao).days
    
    # Validação customizada - NOVO CONCEITO!
    def clean(self):
        if self.livro and not self.livro.pode_ser_emprestado():
            raise ValidationError('Este livro não está disponível para empréstimo.')
        
        if self.usuario and not self.usuario.pode_pegar_emprestado():
            raise ValidationError('Este usuário não pode pegar livros emprestados no momento.')
    
    # Método save customizado
    def save(self, *args, **kwargs):
        # Se é um novo empréstimo, define data de devolução e muda status do livro
        if not self.pk:  # Novo registro
            if not self.data_prevista_devolucao:
                self.data_prevista_devolucao = date.today() + timedelta(days=14)
            self.livro.status = 'emprestado'
            self.livro.save()
        
        # Se está sendo devolvido, muda status do livro
        elif self.data_devolucao and self.livro.status == 'emprestado':
            self.livro.status = 'disponivel'
            self.livro.save()
        
        super().save(*args, **kwargs)