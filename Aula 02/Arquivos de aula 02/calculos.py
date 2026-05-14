#Multiplicação
def multiplicar(numero1, numero2):
    return numero1 * numero2

#Chama a função:
resultado = multiplicar(10, 5)
print (resultado)
# Exibe: 50

#calcular Média
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

#Chama a função:
media_final = calcular_media(8, 10)
print(media_final) 
#Exibe: 9.0

#calcular desconto
def calcular_desconto(valor, desconto):
    return valor - (valor * desconto / 100)

#Chama a função:
resultado = calcular_desconto(100, 15)
print(resultado)
#exibe: 85.0