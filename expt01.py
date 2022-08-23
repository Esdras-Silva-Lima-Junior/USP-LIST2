#Aqui criei um codigo para fazer uma equação de bascara:

#Importando math, muito importante imprimir porque vamos usar a função math.sqrt() para fazer raiz quadrada.
import math

#Abaixo três entradas de dados para A, B e C e é muito importante analisar que formatei os resultados para float(Ponto flutuante) que nessa equação é essencial.
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

#Descobrindo delta com as entradas de valores acima e usando a formula para delta da equação: X = -b +- (raiz quadrada) b² - 4.a.c / 2.a
delta = b ** 2 - 4 * a * c

#Verificando se delta é menor que zero e saber se existe raizes reais.
if delta < 0:
    print("esta equação não possui raizes reais")
else:
    #Aqui para saber se tem apenas uma raiz que é igual a zero.
    if delta == 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        print("a raiz desta equação é", raiz1)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        #Daqui para baixo é apenas para verificar os números e formatar em formato crescente.
        if raiz1 >= raiz2:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print("as raízes da equação são", raiz2,"e",raiz1)
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print("as raízes da equação são", raiz1,"e",raiz2)
#Fimse :D