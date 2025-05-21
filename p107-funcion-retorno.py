#Ejemplifica el uso de valores de retorno en la funcion 
import os
def suma(n1,n2):
    s=n1+n2
    return s
os.system('cls')
print('\nInvocando una funcion con 2 parametros y recibiendo un valor de retorno')
res=suma(10,20)#guardamos el resultado en una variable
print(f'\nEl resultado de la suma es {res}')

res=suma(1000,2000)#guardamos el resultado en una variable
print(f'\nEl resultado de la suma es {res}')



print('\nDame dos numeros enteros y te calculare su suma')
a,b=int(input()), int(input())#leo los valores en variables diferentes a los parametros
print(f'\nLa suma de los numeros que me diste es {suma(a,b):,.2f}')# no se guarda el valor de retorno, solo se muestra