# Ejer1
# Contar palabras
with open ("archivos/datos.txt", "r") as ficheroLectura:
    lineas = ficheroLectura.read()
    palabras = lineas.split()
    print(len(palabras))
ficheroLectura.close()

# Ejer2
# Contar frecuencia de cada palabra
ficheroLectura = open("archivos/datos.txt", "r")
lineas = ficheroLectura.read()
palabras = lineas.split()

diccionario = {}
for palabra in palabras:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1

print(diccionario)
ficheroLectura.close()

# Ejer3
# Mostrar solo lineas que contengan palabra clave
with open ("archivos/datos.txt", "r") as ficheroLectura:
    clave = input("Ingrese clave: ")
    lineas = ficheroLectura.readlines()
    for linea in lineas:
        if clave in linea:
            print(linea)
ficheroLectura.close()

# Ejer4
# Remplazar una palabra en un fichero
with open ("archivos/datos.txt", "r") as ficheroLectura:
    palabra = input("Ingrese la palabra a remplazar: ")
    reemplazo= input("Ingrese la palabra por la cual la quiere cambiar: ")
    contenido = ficheroLectura.read()
    contenido_modificado = contenido.replace(palabra, reemplazo)
ficheroLectura.close()

with open ("archivos/modificado.txt", "w") as ficheroEscritura:
    ficheroEscritura.write(contenido_modificado)
ficheroEscritura.close()


# Ejer5
# Quitar lineas vacias de un fichero
ficheroLectura = open("archivos/datos.txt", "r")
lineas = ficheroLectura.readlines()
for linea in lineas:
    if linea.strip():
        print(linea, end="")
ficheroLectura.close()

# Ejer6
# Ordenar lineas alfabéticamente
ficheroLectura = open("archivos/datos.txt", "r")
lineas = ficheroLectura.readlines()
lineasOrdenadas = sorted(lineas)
print(lineasOrdenadas)
ficheroLectura.close()

# Ejer7
# Mostrar la linea mas larga y mas corta en funcion de caracteres
ficheroLectura = open("archivos/datos.txt", "r")
lineas = ficheroLectura.readlines()
max = max(lineas, key=len)
min = min(lineas, key=len)
print(min+"\n"+ max)
ficheroLectura.close()

# Ejer8
# Comparar ficheros linea por linea

ficheroLectura1 = open("archivos/datos1.txt", "r")
ficheroLectura2 = open("archivos/datos2.txt", "r")

contenido1 = ficheroLectura1.readlines()
contenido2 = ficheroLectura2.readlines()

for i in range(len(contenido1)):
    linea1 = contenido1[i]
    linea2 = contenido2[i]

    if linea1 != linea2:
        print(f"Diferencia en línea {i+1}:")
        print(f"  datos1.txt → {linea1}")
        print(f"  datos2.txt → {linea2}")
ficheroLectura1.close()
ficheroLectura2.close()

# Ejer9
# Indice de palabras
diccionario = {}

with open("archivos/datos.txt", "r") as ficheroLectura:
    for index, linea in enumerate(ficheroLectura, start=1): # Para que empiece en 1 y no en 0
        palabras = linea.split()
        for palabra in palabras:
            if palabra not in diccionario:
                diccionario[palabra] = [index]
            else:
                diccionario[palabra].append(index)

print (diccionario)



