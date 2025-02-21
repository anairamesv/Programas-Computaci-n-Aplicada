#Administrar el ingreso a la universidad de mujeres 
import os;os.system('cls')
print('Universidad Kitty Kat SA\nPara el ingreso a la univerdidad:')
nombre=input('Dame tu nombre: ')
sexo=int(input('Dame tu sexo:\n1 si H \n2 si M '))
edad= int(input('Dame tu edad:'))
c1,c2,c3=input('Dame 3 calificaciones separadas por espacio ').split()
c1,c2,c3=float(c1),float(c2),float(c3)
prom=(c1+c2+c3)/3
if sexo==1:
 print(f'{nombre}, H, con {edad} de edad, con calificaciones: {c1},{c2},{c3}, lo siento, solo aceptamos mujeres')
else:
    if edad>=21:
        prom=(c1+c2+c3)/3
        if prom>=8 and prom<=9.5:
            print(f'{nombre}, con {edad} años, y promedio {prom} has sido ACEPTADA, todos tus datos lo permiten')
        else:
            print(f'{nombre}, M, con {edad} de edad, con calificaciones: {c1},{c2},{c3}, tu promedio no alcanza, solo promedios de 8 a 9.5')

    else:
        print(f'{nombre}, M, con {edad} de edad, con calificaciones: {c1},{c2},{c3}, solo aceptamos mayores de 21 años')
