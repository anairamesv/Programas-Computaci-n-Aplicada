#Dados dos conjuntos de nombres calcular union, interseccion, diferencia y diferencia simetrica

import os;os.system('cls')
A={'Juan','Maria','Pedro','Jose','Rocio'}
B={'Pedro','Juan','Pablo','Mateo','Esther'}
C={'Pablo','Mateo'}
D={'Reynaldo','Angelica'}

print('\nUnión')
print(f'A unión B:{A|B}')

print('\nIntersección')
print(f'A intersección B:{A&B}')

print('\nDiferencia')
print(f'A diferencia B:{A-B}')

print('\nDiferencia simetrica')
print(f'A diferencia simetrica B:{A^B}')

print('\nProbar si subconjunto')
print(f'Pablo y Mateo subconjunto B: {C.issuperset(B)}')

print('\nProbar si superconjunto')
print(f'A superconjunto de Reynaldo y angelica: {A.issubset(D)}')

print('\nVerificar presencia')
print(f'Pedro en A:{'Pedro' in (A)}')
print(f'Lilia en B:{'Lilia' in (B)}')