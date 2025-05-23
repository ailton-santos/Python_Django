from django.shortcuts import render
from .forms import ConteudoForm

# função auxiliar para converter link do YouTube para embed
import re

def embed_youtube(url):
    match = re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)", url)
    return f"https://www.youtube.com/embed/{match.group(1)}" if match else ""

def embed_spotify(url):
    if "spotify" in url:
        return url.replace("open.spotify.com", "open.spotify.com/embed")
    return ""

def cadastrar_conteudo(request):
    dados = None
    if request.method == 'POST':
        form = ConteudoForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            dados['youtube1_embed'] = embed_youtube(dados['youtube1'])
            dados['youtube2_embed'] = embed_youtube(dados['youtube2']) if dados['youtube2'] else None
            dados['spotify_embed'] = embed_spotify(dados['spotify']) if dados['spotify'] else None
    else:
        form = ConteudoForm()

    return render(request, 'conteudos/cadastro.html', {'form': form, 'dados': dados})