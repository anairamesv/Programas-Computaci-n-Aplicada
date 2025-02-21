#Mostrar el dia de la semana correspondiente según un número entre 1 y 7
import os;os.system('cls')
print('Mostrar que dia de la semana es según un número dado')
n=int(input('Dame un número '))
if n<=7 and n>=1:
    print('El día:')
    if n==1:
        print(f'{n} es Domingo')
    elif n==2:
        print(f'{n} es Lunes')
    elif n==3:
        print(f'{n} es Martes')
    elif n==4:
        print(f'{n} es Miércoles')
    elif n==5:
        print(f'{n} es Jueves')
    elif n==6:
        print(f'{n} es Viernes')
    elif n==7:
        print(f'{n} es Sábado')
else:
    print('Día invalido')