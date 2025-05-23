from django.shortcuts import render

def aula_com_midia(request):
    context = {
        'titulo': 'Aula de Introdução ao Python',
        'descricao': 'Nesta aula, vamos aprender os conceitos básicos da linguagem Python.',
        'youtube_embed': 'https://www.youtube.com/embed/rfscVS0vtbw',
        'spotify_embed': 'https://open.spotify.com/embed/track/4cOdK2wGLETKBW3PvgPWqT?utm_source=generator'
    }
    return render(request, 'aulafixa/aula.html', context)
