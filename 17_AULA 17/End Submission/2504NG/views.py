from django.shortcuts import render
from.forms import InstrumentoForm

def enviar_info(request):
    mensagem = ""
    if request.method == "POST":
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            descricao = form.cleaned_data["descricao"]
            numero_de_serie = form.cleaned_data["numero_de_serie"]
            area_de_utilizacao = form.cleaned_data["area_de_utilizacao"]
            
            return render (request, 'instrumento/sucesso.html')
            #mensagem = f"Cadastro realizado com sucesso: {nome}, {descricao}, {numero_de_serie} e {area_de_utilizacao}"
        
    else:
        form = InstrumentoForm()
    
    return render(request, 'instrumento/instrumento.html', {'form':form, 'mensagem': mensagem})

# Create your views here.
