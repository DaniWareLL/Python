# Ejer1-2
# Leer, mostrar el contenido de un fichero y contar sus lineas
contador : int = 0
fichero = open("archivos/datos.txt", "r")
for line in fichero:
    line = line.strip() # Para quitar espacios entre lineas (\n)
    contador += 1
    print(line)
print(contador)
fichero.close()
# contenido = fichero.read() -> t0do el contenido en un string
# contenido = fichero.readlines() -> t0do el contenido en una lista de string
# Tambien puedes hacerlo así pero solo funciona si no lo has leido antes, sino devuelve ""


# Ejer3
# Buscar palabra en un fichero
palabra = input("Ingrese una palabra: ")
fichero =open("archivos/datos.txt", "r")
contador2 : int = 0
for line in fichero:
    if palabra in line:
        contador2 += 1
print(contador2)
fichero.close()


# Ejer4-5
# (w) machaca el contenido del fichero, (a) añade contenido al fichero
fichero = open("archivos/datos.txt", "w")
fichero.write("Esto es una prueba\n"
              "Esto es un salto de linea")
fichero.close()

# Ejer6
# Copiar contenido de un fichero a otro
ficheroLectura = open("archivos/datos.txt", "r")
ficheroEscritura = open("archivos/copiaDatos.txt", "w")

for line in ficheroLectura:
    ficheroEscritura.write(line)
ficheroLectura.close()
ficheroEscritura.close()

# Ejer7
# Invertir el contenido de un fichero
ficheroLectura = open("archivos/datos.txt", "r")
lineas = ficheroLectura.readlines()
ficheroEscritura = open("archivos/reversed.txt", "w")
for line in reversed(lineas):
    ficheroEscritura.write(line+"\n")