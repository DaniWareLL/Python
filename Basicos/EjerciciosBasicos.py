# 1. Calcular la suma de dos números
a = 5
b = 7
suma = a + b
print("1) La suma es:", suma)

# 2. Calcular el área de un círculo
import math
radio = 4
area_circulo = math.pi * radio**2
print("2) El área del círculo es:", area_circulo)

# 3. Convertir grados Celsius a Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("3) ", celsius, "°C son", fahrenheit, "°F")

# 4. Calcular el doble y el triple de un número
num = 8
doble = num * 2
triple = num * 3
print("4) Doble:", doble, " - Triple:", triple)

# 5. Calcular la media de tres números
x = 6
y = 9
z = 12
media = (x + y + z) / 3
print("5) La media es:", media)

# 6. Multiplicar dos números
n1, n2 = 3, 4
producto = n1 * n2
print("6) El producto es:", producto)

# 7. Concatenar dos cadenas de texto
cadena1 = "Daniel"
cadena2 = "Lillo"
resultado = cadena1 + " " + cadena2
print("7) Cadena concatenada:", resultado)

# 8. Mostrar un número repetido varias veces
numero = 7
veces = 5
for i in range (veces):
    print("8) Número repetido:", numero)

# 9. Calcular el área de un rectángulo
base = 10
altura = 6
area_rectangulo = base * altura
print("9) El área del rectángulo es:", area_rectangulo)

# 10. Calcular el perímetro de un rectángulo
perimetro_rectangulo = 2 * (base + altura)
print("10) El perímetro del rectángulo es:", perimetro_rectangulo)

# 11.

hours = 45
rate = 10
result = 0

if hours >= 40:
    rate *= 1.5
    result = hours * rate
    print("El resultado es: ", result)
else:
    result = hours * rate
    print ("El resultado es: ", result)