from django import forms

class AvaliacaoForm(forms.Form):
    nome = forms.CharField(
        label='Seu nome',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome', 'autofocus': True})
    )
    email = forms.EmailField(label='Seu e-mail')
    nota = forms.ChoiceField(
        label='Nota',
        choices=[(str(i), f'{i} Estrela{"s" if i != 1 else ""}') for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    comentario = forms.CharField(
        label='Comentário',
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False
    )
    aceite = forms.BooleanField(
        label='Concordo com os termos de uso'
    )
    produto_id = forms.CharField(
        widget=forms.HiddenInput(),
        initial='XYZ123'
    )