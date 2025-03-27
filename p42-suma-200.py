#Suma de los numeros introducidos por el ususario hasta que la suma sea >=200
import os


while(True):
    s=0
    c=0
    os.system('cls')
    while s<=200:
        n=int(input('Introduce un numero: '))
        s+=n
        c+=1
    print(f'Fueron {c} numeros introducidos\n La suma de estos es: {s}')
    if input('Deseas iniciar de nuevo (S/N)').upper()=='N': break
print('Proceso terminado')