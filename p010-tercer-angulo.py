#Calculo de un 3er angulo a partir de dos ángulos dados

import os; os.system('cls')
print('Calculo del 3er angulo')
a1, a2 = input('Dame dos ángulos separados por un espacio ').split()
a1, a2 = int(a1), int(a2)
a3 = 180 - (a1+a2)
print(f'El ángulo 1 es: {a1}\nEl ángulo 2 es: {a2}\nEl ángulo 3 da: {a3}')

