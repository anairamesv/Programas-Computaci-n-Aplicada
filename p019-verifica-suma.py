#verificar si la suma de dos numeros enteros es igual a un tercero

import os; os.system('cls')

print('Verificar si la suma de dos numeros enteros es igual a un tercero')

print('Dame 3 numeros enteros separados por enter')
n1, n2, n3= int(input()),int(input()),int(input())

if n1+n2==n3:   
    print('n1 + n2 = n3')
elif n1+n3==n2:
    print('n1 + n3 = n2')
elif n2+n3==n1:
    print(f'n2 + n3 = n1')
else:
    print('\nPosiblemente son iguales')