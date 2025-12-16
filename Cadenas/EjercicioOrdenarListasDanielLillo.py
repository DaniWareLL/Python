# Crea un programa que tenga una lista de estudiantes con nombre, edad y puntuacion.
# Posteriormente, pedirás al usuario que introduzca el criterio de ordenación y si es ascendente o no.
# Por último crearás otra lista ordenada como haya pedido el usuario.

estudiantes = [
    {'nombre': 'Ana', 'edad': 20, 'puntuacion': 85},
    {'nombre': 'Carlos', 'edad': 22, 'puntuacion': 92},
]

CLAVE_ORDENACION = input("Introduce el campo por el que quieres ordenar la lista entre: nombre, edad, puntuacion: ")
descendente = input("Introduce true si quieres que sea descendente y false si no: ")

if(descendente == 'true'):
    ORDEN_DESCENDENTE = True
elif(descendente == 'false'):
    ORDEN_DESCENDENTE = False

lista_temporal = []
for estudiante in estudiantes:
    clave_valor = estudiante[CLAVE_ORDENACION]
    lista_temporal.append((clave_valor, estudiante))

lista_temporal.sort(reverse=ORDEN_DESCENDENTE)

estudiantes_ordenados = [tupla[1] for tupla in lista_temporal]

print(f"Resultado (Ordenado por '{CLAVE_ORDENACION}):")
for e in estudiantes_ordenados:
    print(e)