# dada una lista con n numeros impares se entrega suma, promedio, numeros divisibles entre 3 y su suma.

import os; os.system('cls')

nums=[]
num3=[]
s=prom=s3=0
i=1
print('Imprimiendo numeros impares')
n=int(input('Cuantos numeros quieres? '))

while len(nums) < n:
    nums.append(i)
    i+=2   
    n3=i

s=sum(nums)
prom=s/len(nums)
print(f'Numeros impares: {nums}')
print(f'Suma: {s}')
print(f'Promedio: {prom}')
num3=[n3 for n3 in nums if n3%3==0]
print(f'Numeros divisibles entre 3: {num3}')
s3=sum(num3)
print(f'Suma numeros divisibles entre 3: {s3}')
b=int(input('Que numero quiere que buscar?'))
if b in nums:
    p=nums.index(b)
    print(f'El elemento {b}, se encuentra en la posicion {p+1}')
else:
    print(f'El elemento {b}, no se encuentra en la lista')