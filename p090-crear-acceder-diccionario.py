#Crear un diccionario de llave numérica días con los siguientes elementos:
#Mostrar el diccionario
#Acceder y mostrar
import os;os.system('cls')
dias={
    1:'Lunes',
    2:'Martes',
    3:'Miércoles',
    4:'Jueves',
    5:'Viernes',
    6:'Sábado',
    7:'Domingo'
}
for k,v in dias.items():
    print(f'{k:2}:{v}')
    
print(f'El primer elemento: {dias[1]}')
print(f'El último elemento: {dias[7]}')
print(f'El quinto elemento: {dias.get(5)}')
print(f'El séptimo elemento: {dias.get(7)}')
for k,v in dias.items():
    print(f'{k:2}:{v}')