#El programa lee una cadea y devuelve un diccionario con la cantidad de apariciones de cada caracter en la cadena


cadena = input("Introduce una cadena: ")
conteo = {}

# iterar cada carácter en la cadena
for caracter in cadena:
    if caracter in conteo:
        # Si el carácter ya está en el diccionario, incrementar su valor
        conteo[caracter] += 1
    else:
        # Si el carácter no está en el diccionario, agregarlo con valor 1
        conteo[caracter] = 1

# Imprimir el resultado
print("Conteo de caracteres:")
for caracter, cantidad in conteo.items():
    print(f"'{caracter}': {cantidad}")