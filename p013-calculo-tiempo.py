#Conversion de horas a días, minutos y segundos
import os; os.system('cls')

print('Conversión de horas a días, minutos y segundos')
print('Dame la cantidad de horas')
horas=int(input())
dia= horas/24
min= horas*60
seg= min*60

print(f'El equivalente de {horas} horas en días es: {dia}\nen minutos es: {min}\ny en segundos es: {seg}')

