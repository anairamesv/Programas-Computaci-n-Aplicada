#Imprime las tablas de 1 a n, hasta el 10
import os
while(True):
    os.system('cls')
    n=int(input('Hasta que tabla quieres? '))
    m=int(input('Hasta donde? '))
    t=1
    while t<=n:
        print(f'\nTabla {t} \n')
        c=1
        while c<=m:
            print(f'{t}x{c}={t*c}')
            c+=1
        t+=1
    if input('Deseas continuar (S/N)').upper()=='N': break
print('Proceso terminado')
      