#numeros de 1 al 100 usando ciclo for
import os
os.system('cls')

x=int(input('Hasta donde? '))
i=int(input('Incremento? '))

for n in range(1,x+1, i):
    print(n , end= '')

print('\n Llegamos al final')