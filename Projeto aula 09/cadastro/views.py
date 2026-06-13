from django.shortcuts import render
#Conectar ao arquivo models. Impota a classe
from .models import Aluno
#from .models import Turma

def home(request):
    titulo = "Pagina Inicial"
    return render(request, 'alunos/home.html', {'titulo': titulo})

def lista_alunos(request):
    titulo = "Alunos"
    alunos = Aluno.objects.select_related('turma', 'campus').all()
    
    context = {
        'titulo': titulo,
        'lista': alunos,
    }
    
    return render(request, 'alunos/lista.html', context)

def turma(request):
    titulo = "Turma"
    lista = Turma.objects.all()

    context = {"titulo": titulo, 'lista': lista}

    return render(request, 'alunos/lista.html', context)

#def lista_alunos(request):
    # Lista de dicionários com os dados dos alunos (simulando o banco de dados)
    alunos = [
        {"nome": "Ana Silva", "curso": "Desenvolvimento Web", "turma": "2026"},
        {"nome": "Carlos Souza", "curso": "Data Center", "turma": "2024"},
        {"nome": "Mariana Costa", "curso": "Design", "turma": "2025"},
    ]
    
    # Passando a lista para o template através do dicionário de contexto
    context = {
        'alunos': alunos
    }
    
    return render(request, 'alunos/lista.html', context)