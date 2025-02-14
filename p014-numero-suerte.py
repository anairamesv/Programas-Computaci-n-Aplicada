#Obtención del número de la suerte
import math as m
import os;os.system('cls')
print('Obtención del número de la suerte a partir del año de nacimiento')

n=int(input('Introduce el año en que naciste: '))

#n=145

u=n%10
n=n//10
d=n%10
n=n//10
c=n%10
n=n//10
m=n

sum=m+c+d+u
print(f'Haciendo la operación {m} + {c} + {d} + {u}\nTu número de la suerte es: {sum}')