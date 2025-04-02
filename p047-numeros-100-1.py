#numeros de 1 al 100 usando ciclo for
import os
os.system('cls')

x=int(input('Desde donde? '))
i=int(input('Decremento? '))

for n in range(x,0,-i):
    print( n , end= '')

print('\nLlegamos al final')