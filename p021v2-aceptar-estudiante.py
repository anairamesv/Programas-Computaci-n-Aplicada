#Administrar el ingreso a la universidad
#Versión 2
import os; os.system('cls')

print('Universidad patito SA de CV')
nombre=input('Dame tu nombre ')
print('Dame dos calificaciones separadas por espacio ')

c1, c2 = input().split()
c1, c2= int(c1), int(c2)
if c1<8 or c2<8:
    print('Solo aceptamos alumnos con calificaciones mayores a 8')
else:
  edad=int(input('Dame tu edad '))
  if not edad>=18:
    print('Solo aceptamos mayores de 18')
  else:
        print(f'{nombre} bienvenid@ a la Universidad Patito, tu edad de {edad} años y calificaciones {c1} y {c2} lo permiten')
