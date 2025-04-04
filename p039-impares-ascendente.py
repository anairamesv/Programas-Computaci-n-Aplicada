#Imprimir numero impar de forma ascendente de 1 a n

import os

while(True):
    os.system('cls')
    n=int(input('Hasta que numero quieres? '))
    t=1
    s=1
    while t<=n:
        print(f'\n {t} \n')

        t+=2   
        print(f'Hasta aquí, la suma es igual a: {s}' )
        s+=t 
    if input('Deseas continuar (S/N)').upper()=='N':break
print('Proceso terminado')
      