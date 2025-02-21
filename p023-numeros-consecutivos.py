#Dados 3 numeros enteros, verificar si son consecutivos y mandar mensaje confirmando, sino manda mensaje de error
import os; os.system('cls')

print('Verificación de números consecutivos')
print('Dame 3 numeros separados por espacio ')
n1,n2,n3=input().split()
n1,n2,n3=int(n1),int(n2),int(n3)

if n3==n2+1 and n3==n1+2 or n3==n1+1 and n3==n2+2:
    print('Los números son consecutivos')
elif n2==n1+1 and n2==n3+2 or n2==n3+1 and n3==n1+2:
    print('Los números son consecutivos')
elif n1==n2+1 and n1==n3+2 or n1==n3+1 and n1==n2+2:
    print('Los números son consecutivos')
else:
    print('Error')