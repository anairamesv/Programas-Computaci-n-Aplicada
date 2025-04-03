#Tablas de multiplicar con for
import os
while(True):
    os.system('cls')
    t=int(input('Que tabla?   '))
    n=int(input('Hasta donde? '))
    for i in range(1,n+1):
        print(f'{t} x {i} = {t*i}')
    if input('Deseas otra tabla (S/N)? ').upper()=='N': break
print('Proceso terminado')