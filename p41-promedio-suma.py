##Calcula la suma y el promedio de una serie introducida por el teclado hasta introcucir 0.
import os
os.system('cls')

print('Se calcula la suma y el promedio de los números introducidos hasta introducir 0')
c=0
s=0
prom=0
num=1
while(True):
    while(num!=0):
        num=int(input('Numero?'))
        print(f'Numero introducido: {num}')
        c+=1
        s+=num
        prom=s/c 
        print(f'Se introdujeron {c} numeros')
        print(f'La suma de los números introducidos es: {s} \n El promedio es: {prom}')
    if input('Deseas iniciar de nuevo (S/N)').upper()=='N': break
    else:
        c=0
        s=0
        prom=0
        num=1
print('Proceso terminado')