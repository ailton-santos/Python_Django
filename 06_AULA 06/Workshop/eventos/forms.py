from django import forms

class EventoForm(forms.Form):
    nome = forms.CharField(label='Nome do Evento', max_length=100)
    data = forms.DateField(label='Data', widget=forms.DateInput(attrs={'type': 'date'}))
    horario = forms.TimeField(label='Horário', widget=forms.TimeInput(attrs={'type': 'time'}))
    imagem = forms.ImageField(label='Imagem do Evento', required=False)
    categoria = forms.ChoiceField(
        label='Categoria',
        choices=[
            ('palestra', 'Palestra'),
            ('workshop', 'Workshop'),
            ('feira', 'Feira'),
            ('outro', 'Outro'),
        ]
    )
    gratuito = forms.BooleanField(label='Evento Gratuito?', required=False)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea)
