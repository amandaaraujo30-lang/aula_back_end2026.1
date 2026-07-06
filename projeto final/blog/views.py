from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from .models import Post, Comentario
from django.db.models import Q

# Página Inicial
def index(request):
    # 1. Pega todas as postagens ordenadas por data
    posts = Post.objects.all().order_by('-data_criacao')
    
    # 2. Captura o termo digitado na barra de busca (q)
    busca = request.GET.get('q')
    
    if busca:
        # Filtra os posts pelo título ou pelo conteúdo usando a variável certa (posts)
        posts = posts.filter(
            Q(titulo__icontains=busca) | Q(conteudo__icontains=busca)
        )
        
    # 3. Renderiza a página principal com a lista (filtrada ou não)
    return render(request, 'blog/index.html', {'posts': posts})

# Cadastro
def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        if usuario and senha:
            from django.contrib.auth.models import User
            if not User.objects.filter(username=usuario).exists():
                novo_usuario = User.objects.create_user(username=usuario, password=senha)
                auth_login(request, novo_usuario)
                return redirect('index')
    return render(request, 'blog/cadastro.html')

# Login
def login(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
    return render(request, 'blog/login.html')

# Logout
def logout(request):
    auth_logout(request)
    return redirect('index')

# Criar Post
def criar_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    if request.method == 'POST':
        titulo_post = request.POST.get('titulo')
        conteudo_post = request.POST.get('conteudo')
        if titulo_post and conteudo_post:
            Post.objects.create(titulo=titulo_post, conteudo=conteudo_post, autor=request.user)
            return redirect('index')
            
    return render(request, 'blog/criar_post.html')

# Postar o Comentario
def postar_comentario(request, post_id):
    # Se o usuário não estiver logado, não deixa comentar
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        texto_comentario = request.POST.get('comentario')
        
        if texto_comentario:
            # Busca o post correto usando o ID que veio da URL
            post_objeto = Post.objects.get(id=post_id)
            
            # Cria e salva o comentário no banco de dados
            Comentario.objects.create(
                post=post_objeto,
                autor=request.user,
                texto=texto_comentario
            )
            
    # Depois de salvar, recarrega a página inicial
    return redirect('index')

# Deletar o post
def deletar_post(request, post_id):
    # Busca o post que queremos deletar
    post_objeto = Post.objects.get(id=post_id)
    
    # Segurança: Só permite deletar se o usuário logado for o autor do post
    if request.user == post_objeto.autor:
        post_objeto.delete()
        
    # Depois de deletar, volta para a página inicial
    return redirect('index')

# Deletar o comentario
def deletar_comentario(request, comentario_id):
    # Busca o comentário que queremos deletar
    comentario = Comentario.objects.get(id=comentario_id)
    
    # Segurança: Só permite deletar se o usuário logado for o autor do comentário
    if request.user == comentario.autor:
        comentario.delete()
        
    # Depois de deletar, volta para a página inicial
    return redirect('index')

# Deletar a conta
def deletar_conta(request):
    # Só faz sentido deletar se o usuário estiver logado
    if request.user.is_authenticated:
        usuario = request.user
        auth_logout(request) # Faz o logout primeiro
        usuario.delete()     # Apaga o usuário do banco de dados
        
    return redirect('index')