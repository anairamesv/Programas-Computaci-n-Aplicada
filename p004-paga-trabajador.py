# Calcular la paga total de un trabajdor en base a las horas trabajadas y a la paga por hora
#Entrada: nombre, horas, paga
#Salida: paga bruta(antes de impuesto), impuesto (paga * tasa), paga neta (paga despues de impuesto)

print('Calculando la paga de un trabajador \n')

#entrada de datos
nombre=input('Nombre del trabajador: ')
horas= int(input('Horas trabajadas:  '))
paga=float(input('Paga x hora trabajada: '))
tasa=0.03

#Calculos
pagabruta = horas*paga
impuesto = pagabruta*tasa
paganeta = pagabruta-impuesto

#Salida
print('\n Resumen de pagos')
print(f'El trabajador {nombre}, trabajó {horas}, a una paga de {paga} pesos, a una tasa de {tasa} impuesto')
print(f'Paga bruta(antes de impuesto): {pagabruta:,.2f}')
print(f'Impuesto: {impuesto:,.2f}')
print(f'Paga neta (después de impuesto): {paganeta:,.2f}')


