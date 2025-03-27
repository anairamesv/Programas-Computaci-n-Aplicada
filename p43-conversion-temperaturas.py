#Calculo de la temperatura de centigrados a farenheit dados por el usuario 
import os
while(True):
    os.system('cls')
    ic=float(input('Dame la temperatura  inicial en grados celcius'))
    fc=float(input('Dame la temperatura  final en grados celcius'))
    c=ic
    print('-'*25)
    print('Tabla de conversion')
    print('-'*25)
    print('Celcius\tFarenheit')
    print('-'*25)
    while c<=fc:
        f=(ic*(9/5))+32
        print(f'{ic}\t{f}')
        c+=1
        ic=c
    print('-'*25)
    if input('Deseas continuar (S/N)').upper()=='N': break
print('Proceso terminado')