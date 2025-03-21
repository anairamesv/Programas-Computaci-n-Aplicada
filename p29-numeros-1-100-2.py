#imprime numeros de 1 a n
import os; os.system('cls')

n=int(input('Hasta donde?'))
c=1
while c<=n:
    print(c, end=' ')
    c+=1
else:
    print('Valor final de c es',c)
print('Proceso terminado')