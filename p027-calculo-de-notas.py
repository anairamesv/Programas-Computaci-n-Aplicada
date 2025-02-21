#Calculo del promedio dadas 5 calificaciones

import os; os.system('cls')
import math as m
print('Calculo de promedio')
print('Dame 5 calificaciones separadas por un espacio ')
n1,n2,n3,n4,n5=input().split()
n1,n2,n3,n4,n5=float(n1),float(n2),float(n3),float(n4),float(n5)
prom=(n1+n2+n3+n4+n5)/5
print(f'Con las calificaciones: {n1}, {n2}, {n3}, {n4}, {n5}, tienes un promedio de: {prom}')
if prom>=0 and prom<=6:
    print('Quedas reprobado')
elif prom>6 and prom<=7:
    print('Pasas de panzaso')
elif prom>7 and prom<=8:
    print('Muy bien, puedes mejorar')
elif prom>8 and prom<=9:
    print('Excelente, sigue así')
elif prom>9 and prom<=10:
    print('Perfecto, tu esfuerzo valió la pena')
else:
    print('Error')