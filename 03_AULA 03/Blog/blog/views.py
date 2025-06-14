# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao') # Ordena por data
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all().order_by('data_criacao') # Comentários do post
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post # Associa o comentário ao post
            comentario.save()
            return redirect('detalhe_post', pk=post.pk)
    else:
        form = ComentarioForm()
    
    return render(request, 'blog/detalhe_post.html', {'post': post, 'comentarios': comentarios, 'form': form})

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/criar_post.html', {'form': form})

