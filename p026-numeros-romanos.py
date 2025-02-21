#Da el equivalente de un número decimal a un número romano entre 1 y 10

import os;os.system('cls')
print('Resultado de un número decimal a número romano')
print('Dame el número: ')
dec=int(input())
if dec<=10 and dec>=1:
    if dec==1:
        print(f'{dec} es I')
    elif dec==2:
        print(f'{dec} es II')     
    elif dec==3:
        print(f'{dec} es III')     
    elif dec==4:
        print(f'{dec} es IV')     
    elif dec==5:
        print(f'{dec} es V')     
    elif dec==6:
        print(f'{dec} es VI')     
    elif dec==7:
        print(f'{dec} es VII')     
    elif dec==8:
        print(f'{dec} es VIII')     
    elif dec==9:
        print(f'{dec} es IX')     
    elif dec==10:
        print(f'{dec} es X')   
else:
    print('Número inválido')  