from django import forms

class CursoForm(forms.Form):
    nome = forms.CharField(label='Nome do Curso', max_length=100)
    data_inicio = forms.DateField(label='Data de Início', widget=forms.DateInput(attrs={'type': 'date'}))
    carga_horaria = forms.IntegerField(label='Carga Horária (horas)')
    material = forms.FileField(label='Material do Curso (PDF)', required=False)
    areas = forms.MultipleChoiceField(
        label='Áreas Relacionadas',
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ('TI', 'Tecnologia da Informação'),
            ('ENG', 'Engenharia'),
            ('ADM', 'Administração'),
            ('EDU', 'Educação'),
        ]
    )
    descricao = forms.CharField(label='Descrição do Curso', widget=forms.Textarea)