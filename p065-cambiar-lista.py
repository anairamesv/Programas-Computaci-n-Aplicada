#Cambiar elementos en un arreglo numerico

import os; os.system('cls')

nums=[10,9,8.5,6.5,9.8,7,5,6.2,9.5]

print('Modificar elmentos de una lista')
print(f'La lista es {nums}, contine {len(nums)} elementos')

print('Modificar elemento 0 y elemento 1')
nums[0]=7
nums[1]=7

print(f'La lista es {nums}, contiene {len(nums)} elementos')
print('Modificar el ranfo de elementos de la posicion 2 a la 5')
nums[2:5]=9,9,9
print(f'La lista es {nums}, contiene {len(nums)} elementos')