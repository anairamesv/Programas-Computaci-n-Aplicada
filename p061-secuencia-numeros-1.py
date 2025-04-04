#Imprime un cuadro de asteriscos
import os
while(True):
    os.system('cls')
    n=int(input('Dame un numero '))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end='')
        print()
    if input('Deseas repetir (S/N)? ').upper()=='N': break
print('Proceso terminado')