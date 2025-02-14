#Cambio de temperatura de celcius a farenheit

import os; os.system('cls')
print('Conversion de grados celcius a farenheit')
cel=float(input('Dame la temperatura en grados celcius'))
farenheit=(cel*(9/5))+32
print(f'El valor en grados farenheit de {cel} grados celcius es de: {farenheit}')
