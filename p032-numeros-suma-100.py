#Suma numeros hasat dar 100

import os; os.system('cls')
c=0
s=0
while c<200:
    c+=1
    s+=c
    print(c, end='')
    if s>=100:
        print('')
        break
else:
    print('Llegamos a la meta') 
print(f'Suma{s}, numero sumandos para alcanzar la meta {c}')    