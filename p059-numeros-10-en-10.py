#Imprimir numeros del 1 a n de 10 en 10

import os
while(True):
    os.system('cls')
    print('Imprime multiplos de 10 entre 1 y n')
    n=int(input('Hasta donde?           '))
    cm=sm=0
 
    for i in range(1, n+1, 10):
            print(i, end=' ')



    if input('\n\nDeseas continuar (S/N)? ').upper()=='N': break
print('\nHemos llegado al final')