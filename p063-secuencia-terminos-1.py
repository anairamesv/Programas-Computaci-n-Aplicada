#Imprimir en términos armonicos un numero introducido y su suma

import os
import math as m
os.system('cls')

n=int(input('¿Cuantos términos? '))
for x in range(1,n+1):
    f=1
    sum=0
    sec=str(1)
    for i in range(1, x+1):
        na= 1/i
        sum+=na
        if i>f:
            sec=sec+ "+" + "1/"+str(i)+ "!"
        
print(f'{sec}')
print(f'Suma es = {sum}')
