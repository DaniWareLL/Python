# Exercise 1: Write a program which repeatedly reads integers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the integers.
# If the user enters anything other than a integers, detect their mistake using try and except and print an error message
# and skip to the next integers.

total:int = 0
count:int = 0

while True:
    user_input = input("Ingrese un número entero (o 'done' para terminar): ")
    if user_input.lower() == "done":
        break
    try:
        number = int(user_input)
        total += number
        count += 1
    except ValueError:
        print("Error: entrada inválida. Por favor, ingrese un número entero.")

if count > 0:
    average = total / count
    print(f"Total: {total}, Cantidad: {count}, Promedio: {average}")
else:
    print("No se ingresaron números válidos.")

#Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum
# of the numbers instead of the average.

numbers = []

while True:
    user_input = input("Ingrese un número (o 'done' para terminar): ")
    if user_input.lower() == "done":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Error: entrada inválida. Por favor, ingrese un número válido.")

if numbers:
    print(f"Máximo: {max(numbers)}")
    print(f"Mínimo: {min(numbers)}")
else:
    print("No se ingresaron números válidos.")

#Ejercicio Inventado Daniel Lilo:
# Realiza una piramide de asteriscos pidiendo al usuario el número de filas

n = int(input("Introduce el número de filas: "))

for i in range(n):
    espacios = n - i - 1
    asteriscos = 2 * i + 1
    print(" " * espacios + "*" * asteriscos)