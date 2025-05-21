#Dados dos conjuntos de nombres calcular union, interseccion, diferencia y diferencia simetrica

import os;os.system('cls')
A={'Juan','Maria','Pedro','Jose','Rocio'}
B={'Pedro','Juan','Pablo','Mateo','Esther'}

print('\nUnión')
print(f'A unión B:{A|B}')

print('\nIntersección')
print(f'A intersección B:{A&B}')

print('\nDiferencia')
print(f'A diferencia B:{A-B}')

print('\nDiferencia simetrica')
print(f'A diferencia simetrica B:{A^B}')