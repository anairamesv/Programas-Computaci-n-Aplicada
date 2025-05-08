#Crear un diccionario de llaves de cadena países
#Mostrar el diccionario
#Modificar elementos
import os; os.system('cls')
paises={
    'argentina':100,
    'brasil':200,
    'colombia':300,
    'chile':400,
    'ecuador':500,
    'bolivia':600,
    'jamaica':700
}
print('Diccionario original')
for k,v in paises.items():
    print(f'{k:<8}:{v}')

#Modificar elementos
paises['brasil']=250
paises['chile']=450
paises.update({'bolivia':650})
paises.update({'jamaica':750})
print()
print('Diccionario nuevo')
#Mostrar diccionario modificado
for k,v in paises.items():
    print(f'{k:<8}:{v}')
