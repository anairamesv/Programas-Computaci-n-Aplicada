#Muestra las operaciones que se pueden efectuar entre los conjuntos
import os;os.system('cls')

c1={1,2,3,4,5}
c2={5,6,7,8,9,10}
c3={9,10,11,12,13}
c4={3,4,5}

print('Ejemplo de las operaciones entre dos conjuntos')
print(f'c1:{c1}\nc2:{c2}\nc3:{c3}\nc4:{c4}')

print('\nunion')
print(f'c1 union c2:{c1.union(c2)}')
print(f'c1 union c3: {c1|c3}')

print('\ninterseccion')
print(f'c1 interseccion c2:{c1.intersection(c2)}')
print(f'c2 interseccion c3: {c2&c3}')

print('\ndiferencia')
print(f'c1 diferencia c4:{c1.difference(c2)}')
print(f'c2 union c3: {c1-c3}')

print('\ndiferencia simetrica')
print(f'c1 union c2:{c1.symmetric_difference(c2)}')
print(f'c2 union c3: {c2^c3}')

print('\nprobar por subconjuntos')
print(f'c4 subconjunto c1:{c4.issubset(c1)}')
print(f'c3 subconjunto c2: {c3<=c2}')

print('\nprobar por superconjuntos')
print(f'c1 superconjunto c4:{c1.issuperset(c4)}')
print(f'c2 superconjunto c3: {c2>=c3}')

print('\nVerificar la presencia de un elemento en el conjunto')
print(f'c4 en c1:{2 in (c1)}')
print(f'c3 en c2: {c3<=c2}')