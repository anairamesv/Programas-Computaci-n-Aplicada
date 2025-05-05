#Procesar una lista de estudiantes usando una lista de diccionarios
#Se calcula la suma de los promedios y el promedio general del grupo

import os;os.system('cls')

grupo=[
    {'nombre':'Carlos', 'edad':45,'carrera':'Sistemas','promedio':9},
    {'nombre':'Rosario', 'edad':35,'carrera':'Sistemas','promedio':10},
    {'nombre':'Jose', 'edad':30,'carrera':'Electronica','promedio':8}
]
print(f'Grupo completo {grupo} - {len(grupo)}')

while True:
    print('\nDame los datos del estudiante')
    datos={}
    nombre=input('Nombre: ')
    if nombre!='':
        datos['nombre']=nombre
        datos['edad']=int(input('Edad: '))
        datos['carrera']=input('Carrera: ')
        datos['promedio']=float(input('Promedio: '))
        grupo.append(datos)
    else: break

print(f'Grupo completo {grupo} - {len(grupo)}')
#imprimir una tabla con los datos de los autos
print('\n Datos de los estudiantes en forma de tabla\n')
print('-'*50)

#imprimimos los encabezados
for llave in grupo[0].keys():
    print(f'{llave:<12}',end='')
print('-'*50)

#imprimir cada dato de cada auto
for alumno in grupo:
    for v in alumno.values():
        print(f'{v:<12}',end='')
    print()
print('-'*50)
suma=0
for alumno in grupo:
    suma=suma+alumno['promedio']
print(f'La suma de promedios es {suma}')
print(f'El promedio del grupo es {suma/len(grupo)}')