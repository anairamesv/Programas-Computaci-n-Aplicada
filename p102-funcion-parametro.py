#ejemplificar el uso de parametros en una funcion
import os
def saludo(nombre):
    print(f'\nHola {nombre} bienvenido a las funciones en python, tu nombre tiene {len(nombre)} caracteres')

os.system('cls')
print('Mandnado saludos desde una funcion')
saludo('Carlos Castañeda')
saludo('Rocio Soto')
saludo('Teresa Bernal')

nombres=['Hugo','Paco','Luis','Donald']

for nombre in nombres:
    saludo(nombre)
#for s in range(5):
  #  saludo(str(s))