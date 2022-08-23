#Criando um programa que se ele for divizor de 5 ou 3 ele irá mostrar "FizzBuzz" na tela, caso contrario mostrará o número inserido.

#Criando a entrada de dados e a variaveis que irão calcular e guardar os resultados nelas mesmas:
number = int(input("Digite um número: "))
result1 = number % 3
result2 = number % 5 

#Criando uma condicional que irá verificar o resultado e exibir um texto dependendo do resultado das variaveis "result1 e result2":
if result1% 3 == 0 or result2% 5 == 0:
    if number < 0:
        print(number)
    else:
        print("FizzBuzz")
else:
    print(number)
#Fimse :D