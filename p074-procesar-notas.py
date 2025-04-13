#Lee n notas para salir introducir 0
import os; os.system('cls')

nums=[]
mp=[]
n=1
suma=prom=0
print('Lee las notas, se entrega, suma, promedio, nota maxima, nota minima y notas menores al promedio')

while n!= 0:
    n=float(input('Calificacion [1-100] >'))
    if n>=1 and n<=100:
        nums.append(n) 
    else:
        print('>(')

nums.sort()
print(f'\n Son {len(nums)} notas, las cuales son {nums}')

suma=sum(nums)
prom=suma/len(nums)

for n in nums:
    if n<prom:
        mp.append(n)


print('\nEstadisticas')
print(f'La suma es: {suma}')
print(f'El promedio es: {prom}')
print(f'Menores al promedio: {len(mp)} y son {mp} ')
print(f'La nota máxima es: {max(nums)}')
print(f'La nota mínima es: {min(nums)}')