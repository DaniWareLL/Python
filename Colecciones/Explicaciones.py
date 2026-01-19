# Listas
# - Mutable
# - Ordenadas
# - Indexadas por posición
# - Permiten duplicados
# - Colección secuencial
# miLista = list()
miLista = ["uno", "dos", "tres"]
print(miLista)

miLista.append("cuatro")
miLista.remove("cuatro")

# Diccionarios (java map)
# - Mutables
# - Ordenados (desde Python 3.7)
# - Indexados por clave
# - No permiten claves duplicadas
# - Colección de mapeo (clave → valor)
# miDiccionario = dict()
miDic = {"uno": 1, "dos": 2, "tres": 3}

# - Añadir
miDic.update({"cuatro" : 4})

# - Eliminar
miDic.pop("tres")
print(miDic)

print(miDic.items())

# Sacar valor en concreto
print(miDic["uno"])

# Sacar keys
print(miDic.keys())

# Sacar valores
print(miDic.values())


# Tuplas
# - Inmutables
# - Ordenadas
# - Indexadas por posición
# - Permiten duplicados
# - Colección secuencial
# miTupla = tuple(miLista)
miTupla = (1, 2, 3)
miTupla2 = (miLista, miDic)
print(miTupla)
print(miTupla2)