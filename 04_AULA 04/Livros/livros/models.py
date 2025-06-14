from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.autor})"


