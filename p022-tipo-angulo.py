#Muestra el tipo de ángulo a partir de un ángulo dado
import os;os.system('cls')
print('Mostrando el tipo de angulo en baso a los grados')
angulo=int(input('Dame un angulo '))
print(f'El angulo tiene {angulo} grados por lo tanto es un angulo: ',end="")
if angulo<90:
    print('agudo')
elif angulo==90:
    print('recto')
elif angulo>90 and angulo<180:
    print('obtuso')
elif angulo==180:
    print('llano')
elif angulo>180 and angulo<360:
    print('concavo')
else:
   print('Angulo fuera de rango')    
