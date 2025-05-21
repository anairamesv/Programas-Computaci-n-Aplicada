#Ejemplificar el uso de una funcion que recibe n parametros
import os
def saludatodos(*todos):
    print(f'\nSaludos para {todos}')
    print(f'\nTu eres un cliente especial {todos[0]}')
    print(f'\nSaludos a todos los clientes de esta tienda: {'/'.join(todos)}\n')
    for nombre in todos:
        print(f'\n {nombre} - Es un placer contar con tu preferencia en esta tienda ')


os.system('cls')
print('\nInvocando una funcion con varios parametros')

saludatodos('Juan','Pedro','Luis','Gonzalo')
