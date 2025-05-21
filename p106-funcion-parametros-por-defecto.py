##ejemplifica el uso de parametros con valores por defecto
import os
def saluda(nombre='nadie',edad=0):
    print(f'\nHola {nombre}, tienes una edad de {edad}')
os.system('cls')
print('\nInvocar una funcion con un numero distinto de paramteros')
saluda('Luis')
saluda()
saluda('Carlos',25)