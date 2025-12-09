
# Comprueba que una cadena sea un anagrama. Debes tener en cuenta mayúsculas y espacios.

def normaliza(cadena: str):
    # Pasar a minúsculas
    cadena = cadena.lower()

    # Quitar espacios
    cadena = cadena.replace(" ", "")

    # Quitar tildes
    cadena = (cadena.replace("á", "a")
              .replace("é", "e")
              .replace("í", "i")
              .replace("ó", "o")
              .replace("ú", "u")
              .replace("ü", "u"))

    return cadena

def es_anagrama(a: str, b: str):
    return sorted(normaliza(a)) == sorted(normaliza(b))

# Ejemplos
print(es_anagrama("Roma", "amor"))          # True
print(es_anagrama("La cosa", "Sal aco"))    # True
print(es_anagrama("Árbol", "labor"))        # True
print(es_anagrama("Daniel", "Ladino"))      # True
print(es_anagrama("Casa", "Saco"))          # True