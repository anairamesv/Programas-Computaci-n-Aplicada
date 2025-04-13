#leer un mes e imprimir sus dias
import os ; os.system('cls')

mes = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
dias = [31,28,31,30,31,30,31,31,30,31,30,31]


print('Dado el numero del mes y se imprime el mes y sus dias')

while (True):
    m=int(input('Dame un numero del 1 al 12: '))
    if m>=1 and m<=12:
        print(f'Elegiste el mes: {m}')
        print(f'El mes es {mes[m-1]}, los días del mes son {dias[m-1]}')
    else: 
        print('Inserta un numero valido')

    if(input('\nDeseas continuar? (S/N) ')).upper()=='N':break

print('\nProceso terminado')
