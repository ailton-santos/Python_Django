from django import forms

class ConteudoForm(forms.Form):
    titulo = forms.CharField(label='Título do Conteúdo', max_length=100)
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea)
    data = forms.DateField(label='Data de Publicação', widget=forms.DateInput(attrs={'type': 'date'}))
    youtube1 = forms.URLField(label='Link do Vídeo 1 (YouTube)')
    youtube2 = forms.URLField(label='Link do Vídeo 2 (YouTube)', required=False)
    spotify = forms.URLField(label='Link do Spotify (música/playlist)', required=False)
