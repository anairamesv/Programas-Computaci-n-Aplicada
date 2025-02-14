# Calculo del volumen de un cilindro dado su radio y altura
import math as m
import os;os.system('cls')

print('Cálculo del volumen de un cilindro')
print('Dame volumen de radio y altura separados por espacio')
r,l=input().split()
r,l=float(r), float(l)
v=m.pi*(m.pow(r,2))*l
print(f'El volumen de un cilindro con\nradio de: {r} y altura de:{l}\nes: {v:,.2f}')