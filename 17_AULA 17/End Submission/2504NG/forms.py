from django import forms

class InstrumentoForm(forms.Form):
    nome = forms.CharField(label = "Nome do instrumento", max_length=255)
    descricao = forms.CharField(label = "Descrição")
    numero_de_serie = forms.CharField(label = "Número de serie")
    area_de_utilizacao = forms.CharField(label = "Área de utilização")
