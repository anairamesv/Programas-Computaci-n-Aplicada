#Genera dos listas de numeros aleatorios y la suma en una tercera
import os, random;os.system('cls')
lista1=[]
lista2=[]
lista3=[]
MAX=10

print('Genera dos listas de numeros aleatorios y la suma en una tercera\n')

print('Generando dos listas de numeros aleatorios')
for n in range(MAX):
    lista1.append( random.randint(1,100))
    lista2.append( random.randint(1,100))

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
print('\nLa suma de los cuadrados')
for i in range(MAX):
    lista1[i]=lista1[i]**2
    lista2[i]=lista2[i]**2
    lista3.append(lista1[i]+lista2[i])

print(f'La lista 1 elevada al cuadrado: {lista1}')
print(f'La lista 2 elevada al cuadrado: {lista2}')
print(f'Lista 3: {lista3}')