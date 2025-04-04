#El usuario adivina un numero entero al azar entre 1 y 100

import os, random;
while(True):
    os.system('cls')
    ns=random.randint(1,100)
    i=0
    while (True):
        n=int(input('Adivina cual es el numero secreto'))
        i+=1
        if n==ns:
            print(f'Felicidades, adivinaste el numero en {i} intentos')
            break
        elif n<ns:
            print('El numero secreto es mas grande')
        else:
            print('El numero secreto es mas pequeño')
    if input('Deseas continuar (S/N)').upper()=='N': break
print('Proceso terminado')