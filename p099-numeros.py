#Dadas unas listas crear conjuntos
#Realizar operaciones de conjuntos

import os;os.system('cls')
l1=[50,60,70,80,90,100,200]
l2=[60,90,100,300,400,500]
l3=[10,20,60,90,70,100,600,700]
A=set(l1)
print(l1)
B=set(l2)
print(l2)
C=set(l3)
print(l3)

print('\nUnion A y B')
print(A|B)
print('\nUnion B y C')
print(B|C)
print('\nDiferencia A y C')
print(A-C)
print('\nDiferencia simetrica')
print(B^C)
print('\nInterseccion B y C')
print(B&C)

print(f'A es subconjunto de B? {A.issubset(B)}')
print(f'C es subconjunto de A? {C.issubset(A)}')
print(f'100 está en A? {100 in (A)}')
print(f'60 está en A,B,C? {60 in (A and B and C)}')
print(f'900 está en A? {900 in (C)}')