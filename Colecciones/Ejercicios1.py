# Ejercicio1
import math

def calcular_estadisticas(numeros):
    return (max(numeros), min(numeros), sum(numeros) / len(numeros))

# Ejercicio2
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Ejercicio3
def analizar_texto(texto):

    num_caracteres = len(texto)
    palabras = texto.split()
    num_palabras = len(palabras)
    primera_palabra = palabras[0]

    return (num_caracteres, num_palabras, primera_palabra)

# Ejercicio4
def convertir_temperatura(celsius):
    fahrenheit = celsius * 1.8 + 32
    kelvin = celsius + 273.15

    return (fahrenheit, kelvin)

#Ejercicio5
def analizar_numeros(numeros):
    for numero in numeros:
        if numero % 2:
            pares = numero
        else:
            impares = numero
    return (pares, impares, sum(numeros))

#Ejercicio6
def procesar_cadena(cadena):
    return (cadena.upper(), cadena.lower(), len(cadena))

