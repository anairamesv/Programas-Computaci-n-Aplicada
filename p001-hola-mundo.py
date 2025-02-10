#Leer y mostrar un saludo
print('Leyendo datos y enviando un saludo:\n')

nombre=input('Dame tu nombre: ') #Lee cadena
edad=int(input('Dame la edad: ')) #Lee cadena y convierte a entero
peso=float(input('Dame tu peso: ')) #Lee una caden ay convierte a float

print(f'{nombre} bienvenido al lenguaje python, tu edad es {edad} y tu peso es {peso}')
print('\n')
print(type(nombre))
print(type(edad))
print(type(peso))