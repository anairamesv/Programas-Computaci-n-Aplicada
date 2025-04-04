#imprime numeros de 1 a n
import os; os.system('cls')

n=int(input('Desde donde? '))
d=int(input('Decrementos? '))
c=n
while c>=1:
    print(c, end=' ')
    c-=d
else:
    print('Valor final de c es',c)
print('Proceso terminado')