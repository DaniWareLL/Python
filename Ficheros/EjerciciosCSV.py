import csv

# Ejer1
# Leer y mostrar contenido fichero .csv
with open('archivos/datosCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader) # Saltarse cabeceras
    for row in csv_reader:
        print(row)
        for item in row:
            print(item)

# Ejer2
# Contar el numero de filas

contador = 0
with open('archivos/datosCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)
    for row in csv_reader:
        contador+=1
print(contador)

# Ejer3
# Leer y seleccionar una columna (Price)
with open('archivos/datosCSV.csv') as csv_file:
    lector = csv.DictReader(csv_file) #convierte cada fila en un diccionario, usando las cabeceras del archivo como claves
    for row in lector:
        print(row["Price"])

# Ejer4
# Calcular promedio columna numerica

suma = 0
contador = 0
with open('archivos/datosCSV.csv') as csv_file:
    lector = csv.DictReader(csv_file)
    for row in lector:
        suma += float(row["Price"])
        contador+=1
print("El promedio es: "+str(suma/contador))

# Ejer5
# Escribir en csv a partir de una lista

productos = [
    ["Producto", "Precio", "Cantidad"],
    ["Manzana", 1.50, 100],
    ["Banana", 0.80, 150],
    ["Naranja", 0.90, 120]
]

with open("archivos/productos.csv", "w", newline="") as archivo: # Si no se pone newline="" deja filas vacias
    escritor = csv.writer(archivo)
    escritor.writerows(productos)

print("Archivo productos.csv creado correctamente.")

# Ejer6
# Filtrar filas de un archivo csv con salario superior a 6000
with open('archivos/empleados.csv') as csv_file:
    lector = csv.DictReader(csv_file)
    for row in lector: # row -> diccionario {}
        if int(row["Salario"]) > 3000:
            print(row)

# Ejer7
# Añadir filas
with open("archivos/productos.csv", "a", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Grapadora",12.99,50])
    escritor.writerow(["Boligrafo",0.99,500])

# Ejer8
# Añadir filas con Dictwritter

campos = ['Nombre', 'Edad', 'Grado']

estudiantes = [
    {'Nombre': 'Juan', 'Edad': '20', 'Grado': 'A'},
    {'Nombre': 'Ana', 'Edad': '22', 'Grado': 'B'},
    {'Nombre': 'Luis', 'Edad': '21', 'Grado': 'A'}
]

with open('archivos/estudiantes.csv', 'w', newline='') as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()  # Escribir cabecera
    escritor.writerows(estudiantes)  # Escribir múltiples filas

# Ejer9
# Buscar un registro especifico (cliente por su nombre)
with open('archivos/empleados.csv', 'r') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for row in lector:
        if row["Nombre"] == "Juan Perez":
            print(row)

# Ejer10
# Eliminar una fila en concreto

producto_a_eliminar = "Manzana"
filas_filtradas = []

# Leer el archivo original y guardar filas que no coincidan con el producto a eliminar
with open('archivos/productos.csv', 'r') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        if fila['Producto'] != producto_a_eliminar:
            filas_filtradas.append(fila)

# Sobrescribir el archivo CSV con las filas filtradas
with open('archivos/productos.csv', 'w', newline='') as archivo_csv:
    campos = ['Producto', 'Precio', 'Cantidad']
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(filas_filtradas)

print(f"El producto '{producto_a_eliminar}' ha sido eliminado del inventario.")