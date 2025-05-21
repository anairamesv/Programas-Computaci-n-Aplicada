#Ejemplificar el uso de una ffuncion para con dos parametros 
import os
def tabla(t,n):
    for i in range(1,n+1):
        print(f'{t}x{i}={t*i}')

os.system('cls')
print('Imprimiend la tabla que tu decidas, hasta donde lo decidas')
t=int(input('Que tabla? '))
n=int(input('Hasta donde? '))
tabla(t,n)
