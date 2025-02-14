#Se calcula la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados

import math as m
import os; os.system('cls')

print('Se calcula el valor de la hipotenusa de un triangulo rectángulo')
print('Dame el valor de sus lados separados con un espacio')
longlado1, longlado2 = input().split()
longlado1, longlado2 =int(longlado1), int(longlado2)
hipotenusa= m.sqrt(longlado1**2+longlado2**2)

print(f'El valor del lado 1 es: {longlado1}\nEl valor del lado 2 es: {longlado2}\nCon ello el valor de la hipotenusa es de: {hipotenusa}')

