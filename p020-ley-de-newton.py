#Calcular fuerza, masa o aceleración segun elija el usuario de acuerdo a la segunda ley de newton

import os;os.system('cls')
print('Calculando los valores de la segunda ley de newton')
print('Calcular fuerza........ [1]')
print('Calcular masa.......... [2]')
print('Calcular aceleración... [3]')
op=int(input('Elige una opción '))
if op==1:
    print('\nCalculando fuerza ')
    m=int(input('Dame la masa '))
    a=int(input('Dame la aceleración '))
    f=m*a
    print(f'\nLa fuerza es {f}')
elif op==2:
    print('\nCalculando masa')
    f=int(input('Dame la fuerza '))
    a=int(input('Dame la aceleración '))
    m=f/a
    print(f'\nLa masa es {m}')
elif op==3:
    print('\nCalculando aceleración ')
    m=int(input('Dame la masa '))
    f=int(input('Dame la fuerza '))
    a=f/m
    print(f'La aceleración es {a}')
else:
    print('Opción invalida')