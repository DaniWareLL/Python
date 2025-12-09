#Ejercicio 1: Calculadora de operaciones básicas Crea un programa que simule una calculadora.
# El usuario debe introducir dos números y seleccionar una operación: suma, resta, multiplicación o división.
# El programa debe repetirse hasta que el usuario decida salir. Debe manejar errores como división por cero y entrada de datos no numéricos.
import random

op : int = 0
resultado : float = 0

while True:

    print("Introduzca un numero entre: \n")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Salir")
    op = int(input())

    if op == 5:
        break

    print("Introduzca el primer numero: ")
    num1 = int(input())
    print("Introduzca el segundo numero: ")
    num2 = int(input())



    match op:
        case 1:
            total = num1 + num2
            print("El resultado es: ",total)
        case 2:
            total = num1 - num2
            print("El resultado es: ",total)
        case 3:
            total = num1 * num2
            print("El resultado es: ",total)
        case 4:
            try:
                total = num1 / num2
                print("El resultado es: ",total)
            except ZeroDivisionError:
                print("No se puede dividir por 0")

#Ejercicio 2: Tabla de multiplicar Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10.
# Usa un bucle for para generar la tabla. Si el usuario introduce un valor no numérico, muestra un mensaje de error usando try-except.

print("Introduce un numero para generar su tabla de multiplicar hasta el 10: ")
numero = int(input())

for i in range(11):
    print(numero,"x",i,"=",numero*i)

#Ejercicio 3: Adivina el número El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo.
# Después de cada intento, el programa indica si el número es mayor o menor. Usa try-except para validar que la entrada sea numérica.
# El juego termina cuando el usuario acierta.

numeroAleatorio = random.randint(1,100)
prueba : int = 0
contador : int = 0

print("Adivina el numero aleatorio: ")
while prueba != numeroAleatorio:
    try:
        prueba = int(input())
    except ValueError:
        print("ERROR el valor tiene que ser un numero")
        continue
    if prueba < numeroAleatorio:
        print("El numero es mayor, vuelve a intentar")
        contador += 1
    else :
        print("El numero es menor, vuelve a intentar")
        contador += 1

print("Acertado, el numero aleatorio era: ",numeroAleatorio)
print("Intentos: ",contador)

#Ejercicio 4: Comprobar si un número es primo Solicita al usuario un número entero positivo y comprueba si es primo.
# Usa un bucle while para verificar si tiene divisores y muestra el resultado.
# Valida la entrada con try-except. Ejercicio

contador : int = 0
try:
    num: int = int(input("Introduce un número entero positivo: "))
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
    if contador > 2:
        print("El numero no es primo")
    else:
        print("El numero es primo")
except ValueError:
    print("ERROR: El valor tiene que ser un número entero.")



# 5: Números primos hasta N Solicita al usuario un número entero positivo N y muestra todos los números primos desde 2 hasta N.
# Usa un bucle for para recorrer los números y otro bucle while para verificar si son primos.
# Maneja errores si el usuario introduce un valor no válido.


try:
    rango: int = int(input("Introduce un rango entero positivo: "))
    print("Numeros primos en el rango: ")
    for i in range(2, rango + 1):
        contador: int = 0
        for j in range(1, i + 1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            print(j)
except ValueError:
    print("ERROR: El valor tiene que ser un número entero.")

# Ejercicio 6: Análisis de notas de alumnos Crea un programa que almacene en una lista las notas de un grupo de alumnos.
# Utiliza un bucle for para recorrer la lista y:
# 1. Contar cuántos alumnos han aprobado (nota ≥ 5).
# 2. Calcular la nota media del grupo.
# 3. Mostrar la nota más alta y la más baja.

notas = [7.5, 4.0, 6.0, 8.5, 3.5, 9.0, 5.0, 2.0, 10.0, 6.5]

aprobados = 0
suma_notas = 0
nota_maxima = notas[0]
nota_minima = notas[0]

for nota in notas:
    if nota >= 5:
        aprobados += 1
    suma_notas += nota
    if nota > nota_maxima:
        nota_maxima = nota
    if nota < nota_minima:
        nota_minima = nota

media = suma_notas / len(notas)

print(f"Cantidad de alumnos aprobados: {aprobados}")
print(f"Nota media del grupo: {media:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")