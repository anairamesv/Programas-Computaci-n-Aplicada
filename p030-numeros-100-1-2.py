#imprime numeros de 1 a n
import os; os.system('cls')

n=int(input('Desde donde?'))
c=n
while c>=1:
    print(c, end=' ')
    c-=1
else:
    print('Valor final de c es',c)
print('Proceso terminado')