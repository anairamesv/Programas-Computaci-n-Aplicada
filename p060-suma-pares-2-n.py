#Imprimir los pares de 2 a n y su suma
import os
while(True):
    os.system('cls')
    print('Imprime multiplos de m entre 1 y n')
    n=int(input('Hasta donde?           '))
    cm=sm=0
 
    for i in range(2, n+1):
        if i % 2==0:
            print(i, end=' ')
            sm+=i
            cm+=2
    
    print(f'\nLa suma es = {sm}')


    if input('\n\nDeseas continuar (S/N)? ').upper()=='N': break
print('\nHemos llegado al final')