#Verificar cual es el numero mayor de una serie de 3
import os;os.system('cls')

print('Verificación del numero mayor')
print('Dame 3 números enteros separados por un espacio ')
n1,n2,n3=input().split()
n1,n2,n3=int(n1),int(n2),int(n3)
if n1>n2 and n1>n3:
    print(f'{n1} es mayor que {n2} y {n3}')
elif n2>n1 and n2>n3:
    print(f'{n2} es mayor que {n1} y {n3}')
elif n3>n1 and n3>n2: 
    print(f'{n3} es mayor que {n1} y {n2}')
else:
    print('error')