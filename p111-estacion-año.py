#Funcion que procesa un numero entre 1y 4 y regresa la estacion del año con letra

import os
def estacion(n):
    if n==1: est='Primavera'
    elif n==2: est='Verano'
    elif n==3: est='Otoño'
    elif n==4: est='Invierno'
    return est

os.system('cls')
while True:
    n=int(input('Estación (1-4): '))
    if n>=1 and n<=4:
        break

print(f'La estacion del año es {estacion(n)}')