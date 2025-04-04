#Calcular el numero mayor de una serie introducida por el teclado, se detiene al introducir 0.

import os
while(True):
    s=1
    c=0
    n=1
    os.system('cls')
    while n!=0:
        n=int(input('Introduce un numero: '))
        if n>c:
            c=n
        else:
            c=c
    print(f'El número mayor es: {c}')
    if input('Deseas iniciar de nuevo (S/N)').upper()=='N': break
print('Proceso terminado')