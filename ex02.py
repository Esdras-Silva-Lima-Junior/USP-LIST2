#Criando um programa que se ele for divizor de 5 ele irá mostrar "Buzz" na tela, caso contrario mostrará o número inserido.

#Criando a entrada de dados e a variavel que irá calcular e guardar o resultado nela mesma:
number = int(input("Digite um número: "))
result = number % 5

#Criando uma condicional que irá verificar o resultado e exibir um texto dependendo do resultado da variavel "result":
if result % 5 == 0 :
    print("Buzz")
else:
    print(number)
#Fimse :D