#Se tienen datos de trabajadores con ellas se crea un diccionario, se muestra y se itera por los elementos
#Se obtienen la suma de los sueldos y el promedio

import os;os.system('cls')
nombres=['juan','pedro','manuel','elias','maria','felipe','julia','roberto']
sueldos=[4550.22,8456.88,1235.12,9998.00,12345.50,29456.55,12234.00,2000.00]

s=0
p=0

#Se crea el diccionario
trabajadores=dict(zip(nombres,sueldos))
#Se muestra el diccionario
print('Diccionario')
for k,v in trabajadores.items():
    print(f'{k:<8} - {v}')
#Se hace la iteración por el diccionario
#Por las llaves
print('Iterando por llaves')
for llave in trabajadores.keys():
    print(f'{llave:<8}')
print('-'*20)

#Por los valores
print()
print('Iterando por valores')
for v in trabajadores.values():
    print(f'{v:<8}')
    s=s+v
print('-'*20)


#Se muestra el diccionario
print()
print('Iterando por llave y valor')
for k,v in trabajadores.items():
    print(f'{k:<8} - {v}')

p=s/len(trabajadores)
print(f'La suma de los sueldos es: {s}')
print(f'El promedio de los sueldos es: {p}')