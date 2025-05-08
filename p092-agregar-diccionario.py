#Diccionario de cadena ventas
#Mostrar el diccionario
#Agregar elementos

import os;os.system('cls')

ventas={
    'Juan':1550,
    'Jose':2600,
    'Maria':2220
}
print('Diccionario original')
for k,v in ventas.items():
    print(f'{k:<5} - {v}')

ventas['Rocio']=2500
ventas['Mateo']=1567
ventas.update({'Andrea':9567,'Miguel':1234})
print()
print('Diccionario nuevo')
for k,v in ventas.items():
    print(f'{k:<5} - {v}')
