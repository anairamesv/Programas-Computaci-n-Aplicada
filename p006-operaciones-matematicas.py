#Ejemplifica las operaciones matemáticas básicas

import os;os.system('cls')

#dato de prueba
#x=10.5
#y=2.5

x=float(input('Valor de x: '))
y=float(input('Valor de y: '))

suma= x+y
resta=x-y
mult= x*y
div=  x/y
res=  x%y
pot=  x**y
dive= x//y

print(f'Suma: {suma} \n Resta: {resta} \n Multiplicación: {mult}\n División: {div}\n Residuo: {res}\n Potencia: {pot}\n División entera: {dive}')
