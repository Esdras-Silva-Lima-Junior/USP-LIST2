#Criando um programa que se ele for divizor de 3 ele irá mostrar "Fizz" na tela, caso contrario mostrará o número inserido.

#Criando a entrada de dados e a variavel que irá calcular e guardar o resultado nela mesma:
number = int(input("Digite um número: "))
result = number % 3

#Criando uma condicional que irá verificar o resultado e exibir um texto dependendo do resultado da variavel "result":
if result % 3 == 0 :
    print("Fizz")
else:
    print(number)
#Fimse :D