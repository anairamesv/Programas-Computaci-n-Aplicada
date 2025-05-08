#Crear un diccionario de llave de cadena municipios
#Mostrar el diccionario
#Eliminar elementos

import os;os.system('cls')
municipios={
    'apozol':1863,
    'calera':1868,
    'fresnillo':1554,
    'guadalupe':1821,
    'jalpa':1824,
    'jerez':1824,
    'loreto':1931,
    'mazapil':1824,
    'momax':1857
}

print('Diccionario original')
for k,v in municipios.items():
    print(f'{k:<5} - {v}')

#Eliminando los elementos
del municipios['apozol']
municipios.pop('fresnillo')
municipios.popitem()
#Diccionario con eliminaciones
print()
print('Diccionario nuevo')
for k,v in municipios.items():
    print(f'{k:<5} - {v}')
municipios.clear()
#Diccionario final
print()
print('Diccionario final')
for k,v in municipios.items():
    print(f'{k:<5} - {v}')