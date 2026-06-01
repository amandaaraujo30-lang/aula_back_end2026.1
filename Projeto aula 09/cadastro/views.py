from django.shortcuts import render

def lista_alunos(request):
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
    
    return render(request, 'lista.html', context)