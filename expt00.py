#Este programa calcula uma cordenadas e informa se está perto ou longe

#Importando a biblioteca math para usar o math.sqrt():
import math

#Criando entradas de dados e uma variavel que vai calcular e guardar o resultado do calculo: 
x1 = int(input("Digite a cordenada x: "))
x2 = int(input("Digite a outra cordenada de x: "))
y1 = int(input("Digite a cordenada de y: "))
y2 = int(input("Digite a outra cordenada de y: "))
calc_dist = int(math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)))

#Criando uma condicional simples:
if calc_dist >= 10:
    print("longe")
    print(calc_dist)
else:
    print("perto")
    print(calc_dist)
#Fimse :D