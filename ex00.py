#Escreva um programa que receba um número natural na entrada e imprima n! (fatorial) na saída.

#importando count para usar na contagem  
from itertools import count

#Criando variaveis e entrada de dados:
n1 = int(input("Digite o valor de n: "))            
result = 0
count = 1

#Criando um laço while para contar e fazer o calculo:
while count == 10:
    result = n1 & 2
    n1 = n1 - 1
    print(result)
#Mostrando o resultado na tela:
print(result) 
#Fimse :D