#Calcular el area de un triangulo

print('Calculando el area de un triangulo: \n')
print('Dame la base y la altura separadas por un <Enter>')
base, altura =int(input()), int(input())

area=base*altura/2

print(f'La base {base} y la altura {altura} da un area de: {area:,.2f}')
