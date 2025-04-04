
#imprime numeros de 1 a n
import os; os.system('cls')

n=int(input('Hasta donde? '))
d=int(input('Incrementos? '))
c=0
while c<=n:
    print(c, end=' ')
    c+=d
else:
    print('Valor final de c es',c)
print('Proceso terminado')