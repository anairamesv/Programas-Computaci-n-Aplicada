#Convierte temperaturas de farenheit a celcius y viceversa usando funciones

import os
def farenheit(t):
    r=(t*(9/5)+32)
    return r

def celcius(t):
    r=(t-32)*(5/9)
    return r

os.system('cls')
print('[F]Farenheit')
print('[C]Celcius')
op=input('Elige:').upper()

if op=='F':
    t=int(input('Temperatura en celcius: '))
    r=farenheit(t)
    print(f'\nLa temperatura en grados farenheit es: {r}')
elif op=='C':
    t=int(input('Temperatura en farenheit: '))
    r=celcius(t)
    print(f'\n La temperatura en grados celcius es: {r}')
else:
    print('Opcion invalida')

print('Gracias por utilizar este programa')