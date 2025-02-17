#Convertir temperaturas de farenheit a centigrados y viceversa

import os; os.system('cls')
print('Convertir temperaturas de farenheit a centigrados y viceversa ')
print('De Centigrados a Farenheit....[1] ')
print('De Farenheit a Centigrados....[2] ')
op=int(input('Elige '))

if op==1:    
    print('Convirtiendo de centigrados a farenheit... ')
    temp=float(input('Grados centigrados '))
    res=(temp*9/5)+32
    print(f'{temp} grados centigrados equivale a {res} grados farenheit')
else:
    print('Convirtiendo de farenheit a centigrados... ')
    temp=float(input('Grados farenheit '))
    res=(temp-32)*5/9
    print(f'{temp} grados farenheit equivale a {res} grados centigrados')
