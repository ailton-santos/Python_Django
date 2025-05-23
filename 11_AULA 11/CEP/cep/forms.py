from django import forms

class CEPForm(forms.Form):
    cep = forms.CharField(label='Digite o CEP', max_length=9, widget=forms.TextInput(attrs={'placeholder': 'Ex: 01001-000'}))
