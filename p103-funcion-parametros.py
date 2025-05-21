#Ejemplificar una funcion que recibe más de un parametro
import os
def saluda(apaterno, nombre,edad):
    print(f'\n Hola {apaterno}, {nombre}, tienes una edad de {edad}')

os.system('cls')
print('\nInvocando una funion con mas de un parametro')
saluda('Castaneda','Carlos',25)
#saluda('Soto') genera error faltan parametros
#saluda('Soto','Rocio',35,65) genera error, muchos parametro