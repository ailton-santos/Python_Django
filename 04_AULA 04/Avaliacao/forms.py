#formulario/forms.py

from django import forms

class InfoForm(forms.Form):
    nomeProduto = forms.CharField(label = 'Produto', max_length=100)
    descricao = forms.CharField(label = 'Descrição', max_length=100)
    preco = forms.DecimalField(label = 'Preço (R$)', max_digits=10, decimal_places=2)
    quantidadeEstoque = forms.IntegerField(label = 'Quantidade em Estoque')

    CATEGORIAS = [
        ('Bebidas', 'Bebidas'),
        ('Hamburguer', 'Hamburguer'),
        ('Salgados', 'Salgados'),
        ('Sobremesas', 'Sobremesas'),
    ]
    categoria = forms.ChoiceField(label = 'Categoria', choices = CATEGORIAS)


# class AvaliacaoForm(forms.Form):
#     nota = forms.IntegerField(label='Nota (1 a 5)', min_value=1, max_value=5)
#     comentario = forms.CharField(label='Comentário', widget=forms.Textarea, required=False)



class AvaliacaoForm(forms.Form):

    class ClienteForm(forms.Form):
        nomeCliente = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome aqui',  #define o texto que aparecerá dentro do campo de entrada como uma dica
            'autofocus': 'autofocus'  #serve para que o campo receba o foco automaticamente quando a página for carregada
        })
    )

    email = forms.EmailField(label = 'E-mail')
    # idProduto = forms.IntegerField(widget=forms.HiddenInput()) #ver se precisa utilizar o initial como parametro
    preco = forms.DecimalField(label = 'Preço (R$)', max_digits=10, decimal_places=2)
    quantidadeEstoque = forms.IntegerField(label = 'Quantidade em Estoque')

    comentario = forms.CharField(
        label = 'Comentário',
        widget = forms.Textarea(attrs={'rows':4, 'cols':40}) #rows define o número de linhas visíveis(neste caso, 4 linhas) e cols define o número de caracteres visíveis por linha (neste caso, 40 caracteres)
    )

    aceiteTermos = forms.BooleanField(
        label = 'Aceito os termos e condições',
        required = True, #para tornar o campo obrigatório
        initial = False, #para garantir que o checkbox comece desmarcado
        error_messages = {'required': 'Você precisa aceitar os termos e condições para prosseguir.'}
    )

# class AvaliacaoForm(forms.Form):
#     nota = forms.ChoiceField(
#         label='Nota',
#         choices=[(str(i), str(i)) for i in range(1, 6)],
#         widget=forms.RadioSelect
#     )
#     comentario = forms.CharField(
#         label='Comentário',
#         widget=forms.Textarea,
#         max_length=500
#     )

