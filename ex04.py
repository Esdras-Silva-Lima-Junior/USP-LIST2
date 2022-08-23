#Criando um programa que informa se os números digitados estão em formato crescente ou não.

#Abaixo as entradas de dados:
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um novo número: "))
n3 = int(input("Digite mais um número: "))

#Nesta verificação com if e else eu usei o operador lógico and para ver se eles são crescentes ou não:
if n2 > n1 and n3 > n2:
    print("crescente")
else:
    print("não está em ordem crescente")
#Fimse :D