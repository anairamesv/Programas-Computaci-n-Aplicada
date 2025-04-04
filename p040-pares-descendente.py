#Imprimir numero pares de forma descendente del 100 a n

import os

while(True):
    os.system('cls')
    print('Imprime los numeros del 100 al numero elegido')
    n=int(input('Hasta que numero quieres? '))
    t=100
    s=100
    while t>=n:
        print(f'\n {t} \n')

        t-=2   
        print(f'Hasta aquí, la suma es igual a: {s}' )
        s+=t 
    if input('Deseas continuar (S/N)').upper()=='N':break
print('Proceso terminado')
      