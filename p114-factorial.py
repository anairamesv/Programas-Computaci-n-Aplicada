#Calcula el facotrial de un numero
import os
def factorial(n):
    f=1
    for n in range(1,n+1):
        f=f*n
    return f


os.system('cls')
print('Dame un numero y te regreso el factorial')
n=int(input('Numero: '))
f=factorial(n)
print(f'\nEl factorial de {n} es {f}')