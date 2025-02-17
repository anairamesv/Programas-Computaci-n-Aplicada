# Calcular la paga de un trabajador considerando que las horas extra de pagan doble

import os; os.system('cls')

print('Calcular la paga de un trabajador considernado que las horas extras se pagan al doble')
nombre=input('Nombre del trabajador ')
horas=int(input('Horas trabajadas '))
paga=float(input('Paga X Hora '))

extra=pextra=total=0 # asignamos el valor de cero a las 3 variables

if horas>40:
    extra=horas-40
    pextra=extra*(2*paga)
    total=(40*paga)+pextra
else:
    total=paga*horas

print(f'{nombre} trabajó {horas} horas, con una paga de {paga} pesos, paga extra {pextra} pesos, pago total {total}')

