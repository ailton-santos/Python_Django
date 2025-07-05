from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=100, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    biografia = models.TextField(blank=True)
    
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
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    ano_publicacao = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2030)]
    )
    paginas = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.autor.nome}"
    
    class Meta:
        ordering = ['-data_cadastro']