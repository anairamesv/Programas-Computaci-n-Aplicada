#ejemplifica la remocion de elementos de una lista de numeros
import os;os.system('cls')
nums=[1,3,5,7,9,11,99,15,88,19,100]
print('Eliminar elementos de una lista usando remove()')
print(f'La lista {nums}, tiene {len(nums)} elementos')
print('Remover la primera ocurrencia de un elemento')
nums.remove(99)
print(f'La lista {nums}, tiene {len(nums)} elementos')
print('Remover un elemento en una posicion determinada y guardarlo usando pop(x)')
num=nums.pop(8)
print(f'La lista {nums}, tiene {len(nums)} elementos, elemento removido{num}')

print('Remover el ultimo elemento de la lista y guardarlo usando pop()')
num=nums.pop()
print(f'La lista {nums}, tiene {len(nums)} elementos, elemento removido{num}')

print('Remover un rango de valores en una lista, usando del')
del nums[2:5]
print(f'La lista {nums}, tiene {len(nums)} elementos')
print('Eliminar todos los elementos de la lista usando clear()')
nums.clear()
print(f'La lista {nums}, tiene {len(nums)} elementos')