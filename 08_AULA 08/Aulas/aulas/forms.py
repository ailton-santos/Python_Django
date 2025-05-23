from django import forms

class AulaForm(forms.Form):
    titulo = forms.CharField(label='Título da Aula', max_length=100)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea)
    data = forms.DateField(label='Data da Aula', widget=forms.DateInput(attrs={'type': 'date'}))
    professor = forms.CharField(label='Professor', max_length=100)
    audio = forms.FileField(label='Áudio da Aula')
    nivel = forms.ChoiceField(
        label='Nível',
        choices=[
            ('iniciante', 'Iniciante'),
            ('intermediario', 'Intermediário'),
            ('avancado', 'Avançado')
        ]
    )
