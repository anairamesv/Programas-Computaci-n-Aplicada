#ejemplifica como se itera sobre una lista de numeros
import os;os.system('cls')
nums=[2,4,6,8,10,12,14,16]
print('Diferentes formas de iterar (pasar por todos los elementos de una lista)')
print(f'Los numeros son {nums}, longitud {len(nums)} elementos')
print('1.-Iterear sobre la lista usando un ciclo for sin subindice')
for n in nums:
    print(n, end=' ')
    
print('2.-Iterar sobre la lista usando un ciclo for con subindice')
for _ in range(len(nums)):
    print(nums[_], end=' ')
    
print('1b.-Iterar sobre la lista, imprimmir cada valor sumandole 2')
for n in nums:
    print(n+2, end=' ')
print(f'Los numeros son {nums}, longitud {len(nums)} elementos')

print('2b.-Iterar sobre la lista, usando el subindice para modificar')
for _ in range(len(nums)):

    print(nums[_], end=' ')
    nums[_]=nums[_]**2
print(f'Los numeros son {nums}, longitud {len(nums)} elementos')

