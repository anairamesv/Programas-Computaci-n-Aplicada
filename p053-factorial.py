#Calcular el factorial de un numero
import os
os.system('cls')
print('calcula el factorial de un numero entero')
n=int(input('Dame un numero entero: '))

f=1
sec=""
for i in range(1, n+1):
    f=f*i
    sec=sec+str(i)+" * "
    if i<n:
        sec=sec+"*"
print(f'{n}! = {sec} = {f:,}')