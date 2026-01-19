# String
# - Inmutables
# - Ordenadas
# - Indexadas por posición
# - Permiten duplicados
# - Colección secuencial (secuencia de caracteres)
# - Se crean con comillas simples o dobles
# - Se pueden concatenar con +
# - Se convierten a número con int() o float()
miString = "Hola"
otro = 'Mundo'
concatenado = miString +" "+ otro
print(concatenado)

# - Acceso por posición usando []
fruta = "banana"
print(fruta[1])   # a

# - len() devuelve el número de caracteres
fruta = "banana"
print(len(fruta))  # 6

# - sorted() devuelve la cadena ordenada
print(sorted("banana", reverse = False))

# - Recorrer Strings
for letra in "banana":
    print(letra)

s = "Blyat Python"
print(s[0:4])  # Mont
print(s[6:])   # Python
print(s[:2])   # Mo


# - Contar Caracteres
palabra = "banana"
contador = 0
for letra in palabra:
    if letra == "a":
        contador += 1
print(contador)

# - Comprueba si un string está dentro de otro
# - Devuelve True/False
"nan" in "banana"  # True


# - Metodos
greet = "Hello Bob"
print(greet.lower())      # hello bob
print(greet.find("Bob"))  # 6
print(greet.replace("Bob", "Jane"))

texto = "   Hola Mundo   "
print(texto.strip())   # "Hola Mundo"
print(texto.lstrip())  # "Hola Mundo   "
print(texto.rstrip())  # "   Hola Mundo"

texto = "uno,dos,tres"
partes = texto.split(",")
print(partes)  # ['uno', 'dos', 'tres']


# Busqueda
data = "From stephen@uct.ac.za Sat Jan 5"
at = data.find("@")
esp = data.find(" ", at)
host = data[at+1 : esp]
print(host)  # uct.ac.za