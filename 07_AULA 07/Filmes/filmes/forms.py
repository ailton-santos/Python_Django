from django import forms

class FilmeForm(forms.Form):
    nome = forms.CharField(label='Nome do Filme', max_length=100)
    data_lancamento = forms.DateField(label='Data de Lançamento', widget=forms.DateInput(attrs={'type': 'date'}))
    categoria = forms.ChoiceField(
        label='Categoria',
        choices=[
            ('acao', 'Ação'),
            ('drama', 'Drama'),
            ('comedia', 'Comédia'),
            ('terror', 'Terror'),
            ('outro', 'Outro'),
        ]
    )
    capa = forms.ImageField(label='Capa do Filme', required=False)
    trailer = forms.URLField(label='Link do Trailer (YouTube)', required=False)
    nota = forms.IntegerField(
        label='Nota (0 a 10)',
        widget=forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 10, 'step': 1})
    )
    sinopse = forms.CharField(label='Sinopse', widget=forms.Textarea)