#Tabla de conversion de peso a dolar en un rango de valores

import os;
while(True):
    os.system('cls')
    tc=20.50 ; tl=25.97
    print('Tabla de conversion de peso a dolar')
    pi=float(input('Valor inicial:'))
    pf=float(input('Valor final:'))
    c=pi
    print('Peso\tDolar\tLibra')
    print('-'*25)
    while c<=pf:
        print(f'{c}\t{c/tc:.2f}\t{c/tl:.2f}')
        c+=1
    print('-'*25)
    if input('Deseas continuar (S/N)').upper()=='N': break
print('Proceso terminado')