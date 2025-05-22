#Se procesara los datos de usuario de empleados en una muebleria
import os;os.system('cls')

print('Mueblería Muebles Dico')
print('Sistema de Procesamiento de Empleados')
print('Captura de datos de los empleados (* para terminar):\n')

empleados = []

while True:
    nombre = input('\nNombre: ')
    if nombre == '*':
        print('Captura de datos terminada.')
        break
    edad = int(input('Edad: '))
    sexo = input('Sexo (h/m): ').lower()
    sueldo = float(input('Sueldo: '))
    pasatiempos = input('Pasatiempos (separados por coma): ').lower()


    empleado = {
        'nombre': nombre,
        'edad': edad,
        'sexo': sexo,
        'sueldo': sueldo,
        'pasatiempos': [p.strip() for p in pasatiempos.split(',')] # separar por comas y quitar espacios y la convierte a lista

    }
    empleados.append(empleado)

print('\nDatos guardados en la lista de diccionarios:')
print(empleados)

print('\nTabla de datos:')
print(f'{'Nombre':<10} {'Edad':<5} {'Sexo':<6} {'Sueldo':<10} Pasatiempos')
for e in empleados:
    print(f'{e['nombre']:<10} {e['edad']:<5} {e['sexo']:<6} {e['sueldo']:<10,.2f} {', '.join(e['pasatiempos'])}') # .join() une los elementos de la lista con una coma y un espacio

# Procesamiento de resumen
total= len(empleados)
hombres = 0
mujeres = 0
pasatiempos_total = {}
sedades = 0
ssueldo = 0
mayor = None
menor = None

for e in empleados:
    if e['sexo'] == 'h':
        hombres += 1
    elif e['sexo'] == 'm':
        mujeres += 1

    sedades += e['edad']
    ssueldo += e['sueldo']

    for p in e['pasatiempos']:
        if p in pasatiempos_total:
            pasatiempos_total[p] += 1
        else:
            pasatiempos_total[p] = 1

    if mayor is None or e['edad'] > mayor['edad']:
        mayor = e
    if menor is None or e['edad'] < menor['edad']:
        menor = e

pedad = sedades / total 
psueldo = ssueldo / total 

print("\nResumen:")
print(f"Empleados : {total}")
print(f"Mujeres   : {mujeres}")
print(f"Hombres   : {hombres}")

print("Pasatiempos:", end=" ")
print(", ".join([f"{k}/{v}" for k, v in pasatiempos_total.items()])) 

print(f"Edad -> suma: {sedades}, promedio: {pedad:.1f}")
print(f"Sueldo -> suma: {ssueldo:,.2f}, promedio: {psueldo:,.2f}")
print(f"{mayor['nombre']} de {mayor['edad']} es el mayor, {menor['nombre']} de {menor['edad']} es el menor.")

