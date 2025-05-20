from django import forms

class ProdutoForm(forms.Form):
    nome = forms.CharField(label='Nome do Produto', max_length=100)
    descricao = forms.CharField(widget=forms.Textarea, label='Descrição')
    preco = forms.DecimalField(label='Preço', max_digits=10, decimal_places=2)
    estoque = forms.IntegerField(label='Quantidade em Estoque')
    categoria = forms.ChoiceField(
        label='Categoria',
        choices=[
            ('Eletrônico', 'Eletrônico'),
            ('Eletrodoméstico', 'Eletrodoméstico'),
            ('Móvel', 'Móvel'),
            ('Outro', 'Outro')
        ]
    )
