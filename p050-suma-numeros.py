#Suma de n numeros introducidos por el ususario usando un ciclo for

import os
while(True):
    os.system('cls')
    cuantos=int(input('Cuantas calificaciones desea procesar? '))
    suma=0
    cadnum = ""
    for i in range(1, cuantos+1):
        n=int(input(f'Numero [{i}]= '))
        suma+=n
        cadnum = cadnum+''+ str (n)
    print(f'Los numeros que intodujiste fueron {cadnum}')
    print(f'La suma es {suma}, el promedio es {suma/n}')


    if input('\n\nDeseas continuar (S/N)? ').upper()=='N': break
print('\nHemos llegado al final')