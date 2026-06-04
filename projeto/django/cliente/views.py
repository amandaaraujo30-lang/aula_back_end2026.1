from django.shortcuts import render #Ja vem por padrão

#Importar a classe (Ferramenta) HttpResponse
from django.http import HttpResponse #Vai responder a solicitação do navegador

#Cria a função que reposnde a solicitação do navegador

#Aula 08
#Chamar arquivos HTML (Template)
def home(request):
    titulo = "Pagina Inicial"
    return render(request, 'clientes/home.html', {'titulo': titulo})
 
def dados_clientes(request):
    titulo = "Nosos Clientes"
    nossos_clientes = [
        {'nome': 'Mario Silva de Carvalho', 'idade': '44 anos', 'nascimento': '17/08/1982'},
        {'nome': 'Jose Alves', 'idade': '42 anos', 'nascimento': '17/08/1980'},
        {'nome': 'Ana Maria Braga', 'idade': '35 anos', 'nascimento': '10/12/1988'},
    ]
    return render(request, 'clientes/dados_clientes.html', {'titulo': titulo, 'dados_clientes':nossos_clientes})
 
def formulario(request):
    titulo = "Nosos Clientes"
    return render(request, 'clientes/form.html', {'titulo':titulo})