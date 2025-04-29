#Ejemplo de uso de un diccionario
import os;os.system('cls')

estudiante={
    'nombre':'Juan Perez',
    'edad': 45,
    'email':'jperez@msn.com',
    'carrera':'Sistemas'
}
estudiante2={
    'nombre':'Maria Juarez','edad': 35,'email':'maria@msn.com','carrera':'Ingenieria','calificacion':9
}
print(f'El diccionario:{estudiante}, elementos{len(estudiante)}')

#modificar /agregar
estudiante['calificacion']=9.5 #agregar
estudiante['email']='juanp@gmail.com' #modificar
print(f'\nEl diccionario:{estudiante}, elementos{len(estudiante)}')
#iterar
print('\n Iterar por las llaves')
for k in estudiante.keys():
    print(k)

print('\nIterar por los valores')
for v in estudiante.values():
    print(v)

print('\nLlaves y valores')
for k,v in estudiante.items():
    print(f'{k:<13}:{v}')

print(f'Suma de las edades:{estudiante['edad'] + estudiante2['edad']}')

print(f'Promedio calificaciones:{(estudiante['calificacion'] + estudiante2['calificacion'])/2}')