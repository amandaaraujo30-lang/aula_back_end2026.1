from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import IntegrityError
from decimal import Decimal

from .models import Cliente, Conta, Movimento
import random

# Função da pagina inicial
def index(request):
    return render(request, 'pages/home.html')

def abrir_conta(request):
    #O metodo post só existe se clicar no botão do formulario
    if request.method == "POST":
        nome_form = request.POST.get('nome') #Capturar o nome que foi digitado no formulario
        cpf_form = request.POST.get('cpf') #Captura o cpf digitado no formulario
 
        #Retira pontos, traços e espaços (Padroniza o cpf)
        cpf_limpo = cpf_form.replace('.', '').replace('-', '').replace(' ','')
 
        if Cliente.objects.filter(cpf=cpf_limpo).exists():
            #Cria a mensagem de erro
            messages.error(request, 'CPF já cadastrado! Use outro CPF ou acesse uma conta existente.')
            return render(request, 'pages/abrir_conta.html')
       
        try:
            #Cadastrar o cliente no banco de dados
            #CRUD - Create,Read,Update,Delete
            cliente = Cliente.objects.create(nome=nome_form, cpf=cpf_limpo)
 
            #Gerar o numero da conta de forma aleatoria
            numero = str(random.randint(10000, 99999))
 
            #Verifica se a conta existe
            while Conta.objects.filter(numero=numero).exists():
                 numero = str(random.randint(10000, 99999))
           
            #Cria a conta
            conta = Conta.objects.create(numero=numero, cliente=cliente)
 
            #Messagens dizendo que a conta foi criada
            messages.success(request, f'Conta criada com sucesso! Seu numero de conta é: {numero}')
       
            return redirect('conta', conta_id=conta.id)

        #Verifica erro de integridade
        except IntegrityError:  #Verifica a integridade do banco de dados (Caso exista um cliente com o mesmo CPF)
            messages.error(request, 'Erro ao criar conta. CPF já cadastrado')
            return render(request, 'pages/abrir_conta.html')
       
        except Exception as e: #Exibe erros aleatorios
            messages.error(request, f'Erro ao cria a conta: {str(e)}')
            return render(request, 'pages/abrir_conta.html')
   
 
    return render(request, 'pages/abrir_conta.html')

def conta(request, conta_id):

    conta = get_object_or_404(Conta, id=conta_id)

    return render (request, 'pages/conta.html', {'conta':conta})

def depositar(request, conta_id):
    
    conta = get_object_or_404(Conta, id=conta_id)

    if request.method == "POST":
        try:
            valor = Decimal(request.POST.get('valor_form'))
            if valor > 0:
                conta.depositar(valor)

                Movimento.objects.create(conta=conta, tipo='deposito', valor=valor)
                messages.success(request, f"Depósito de R${valor:.2f} realizado")

                return redirect('conta', conta_id=conta.id)
            else:
                messages.error(request, 'Valor invalido!')
        except:
            messages.error(request, 'Valor invalido!')

    return render(request, 'pages/depositar.html', {'conta':conta})