#Muestra las operaciones basicas sobre conjuntos

import os;os.system('cls')

muns={'Zacatecas','Guadalupe','Jerez','Fresnillo','Fresnillo'}

print('\nEjemplificando las operaciones basicas de conjuntos')
print(f'El conjunto: {muns}-{len(muns)} ')

print('\nLista de municipios usando un ciclo')
for m in muns:
    print(m,end=' ')

print('\nZacatecas está en el conjunto de municipios?','Zacatecas' in muns)

print('\nAgregar un elemento al conjunto')
muns.add('Teul')
print(f'El conjunto: {muns}-{len(muns)} ')

print('\nAgregar varios elementos a un conjunto')
otros={'Luis Moya','Ojocaliente','Tepetongo'}
muns.update(otros)
print(f'El conjunto: {muns}-{len(muns)} ')

print('\nEliminar elementos de un conjunto')
muns.remove('Zacatecas')
muns.discard('Ojocaliente')
muns.pop()
print(f'El conjunto: {muns}-{len(muns)} ')

print('\nEliminar todos los elementos del conjunto')
muns.clear()
print(f'El conjunto: {muns}-{len(muns)} ')