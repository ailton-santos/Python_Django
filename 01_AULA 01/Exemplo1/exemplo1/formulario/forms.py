# formulario/forms.py
from django import forms

class InfoForm(forms.Form):
    nome = forms.CharField(label='Seu Nome', max_length=100)
    email = forms.EmailField(label='Seu E-mail')
