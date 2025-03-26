#Imprime la tabla de multiplicar t, hasta n
import os
while(True):
    os.system('cls')
    print('Imprimiendo tabla de multiplicar')
    t=int(input('Que tabla quieres? '))
    n=int(input('Hasta donde? '))
    k=1
    
    while k<=n:
        print(f'{t}x{k}={t*k}')
        k+=1
    if input('Deseas continuar (S/N)').upper()=='N': break
print('Proceso terminado')
    