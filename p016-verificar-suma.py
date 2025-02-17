#verificar si la suma de dos numeros enteros es igual a un tercero

import os; os.system('cls')

print('verificar si la suma de dos numeros enteros es igual a un tercero')

print('Dame 3 numeros enteros separados por enter')
n1, n2, n3= int(input()),int(input()),int(input())

if n1+n2==n3:   
    print('La suma de los dos primeros números es igual al tercero')
else:
    print('\nLa suma de los dos primeros numeros NO es igual al tercero\n')

    print('\nGracias por utilizar este programa')