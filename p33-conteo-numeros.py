#Contar numeros, los suma, los cuenta: positivos, negativos, ceros, sale con 999
import os; os.system('cls')

c=s=0
cp=cn=cc=0

while(True):
    num=int(input('Numero?'))
    if num==999:
        break
    else:
        c+=1
        s+=num
        if num>0: cp+=1
        elif num<0: cn+=1
        else: cc+=1
print(f'Se introdujeron {c} numeros')
print(f'La suma es: {s}')
print(f'Positivos {cp}')
print(f'Negativos {cn}')
print(f'Ceros {cc}')

print('Gracias por utilizar este programa')