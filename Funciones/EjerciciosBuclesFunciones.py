import random

# 1)
def calculadora():
    while True:
        print("\nSeleccione una operación:")
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicación")
        print("4) División")
        print("5) Salir")
        try:
            op = int(input("Opción: "))
        except ValueError:
            print("ERROR: Introduce un número válido.")
            continue

        if op == 5:
            break

        try:
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
        except ValueError:
            print("ERROR: Debes introducir números enteros.")
            continue

        match op:
            case 1:
                print("Resultado:", num1 + num2)
            case 2:
                print("Resultado:", num1 - num2)
            case 3:
                print("Resultado:", num1 * num2)
            case 4:
                try:
                    print("Resultado:", num1 / num2)
                except ZeroDivisionError:
                    print("ERROR: No se puede dividir por cero.")
            case _:
                print("Opción no válida.")

# 2)
def tabla_multiplicar():
    try:
        numero = int(input("Introduce un número para su tabla de multiplicar: "))
        for i in range(11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("ERROR: Debes introducir un número entero.")

# 3)
def adivina_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    print("Adivina el número entre 1 y 100:")

    while True:
        try:
            intento = int(input("Tu intento: "))
        except ValueError:
            print("ERROR: Debes introducir un número.")
            continue

        intentos += 1
        if intento < numero_aleatorio:
            print("El número es mayor.")
        elif intento > numero_aleatorio:
            print("El número es menor.")
        else:
            print(f"¡Correcto! El número era {numero_aleatorio}. Intentos: {intentos}")
            break

# 4)
def es_primo():
    try:
        num = int(input("Introduce un número entero positivo: "))
        if num < 2:
            print("El número no es primo.")
            return
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("El número no es primo.")
                return
        print("El número es primo.")
    except ValueError:
        print("ERROR: Debes introducir un número entero.")

# 5)
def primos_hasta_n():
    try:
        n = int(input("Introduce un número entero positivo: "))
        print("Números primos hasta", n)
        for i in range(2, n + 1):
            es_primo = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    es_primo = False
                    break
            if es_primo:
                print(i, end=" ")
        print()
    except ValueError:
        print("ERROR: Debes introducir un número entero.")

# 6)
def analisis_notas():
    notas = [7.5, 4.0, 6.0, 8.5, 3.5, 9.0, 5.0, 2.0, 10.0, 6.5]
    aprobados = sum(1 for nota in notas if nota >= 5)
    media = sum(notas) / len(notas)
    nota_max = max(notas)
    nota_min = min(notas)

    print(f"Cantidad de alumnos aprobados: {aprobados}")
    print(f"Nota media del grupo: {media:.2f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")


#***********************************************************

# 1)
def calcular_inversion(inversion_inicial: int, interes_anual: float, años: int) -> float:
    inversion = inversion_inicial
    for _ in range(años):
        inversion += inversion * (interes_anual / 100)
    return inversion

def ejecutar_inversion():
    print("¿Cuánto quieres invertir?")
    inversion = int(input())
    print("Indique el interés anual:")
    interes = float(input())
    print("¿Durante cuántos años?")
    años = int(input())
    resultado = calcular_inversion(inversion, interes, años)
    print(f"Inversión final: {resultado:.2f}")

# 2)
def cuenta_regresiva(numero: int):
    for i in range(numero, 0, -1):
        print(i, ",", end="")
    print()

def ejecutar_cuenta_regresiva():
    print("Introduce un número positivo:")
    numero = int(input())
    cuenta_regresiva(numero)

# 3)
def primer_multiplo_de_7(inicio: int, fin: int):
    for i in range(inicio, fin):
        if i % 7 == 0:
            print(f"Primer múltiplo de 7: {i}")
            break

def ejecutar_multiplo():
    primer_multiplo_de_7(80, 200)

# 4)
inventarioCantidades = []
inventarioNombres = []

def añadir_stock(inventarioCantidades, inventarioNombres):
    try:
        print("Introduzca cantidad:")
        cantidad = int(input())
        print("Introduzca producto:")
        producto = input()
        inventarioCantidades.append(cantidad)
        inventarioNombres.append(producto)
    except ValueError:
        print("Introduce un número válido")

def vender_producto(inventarioCantidades, inventarioNombres):
    print("Introduce el tipo de producto a borrar:")
    productoEliminar = input()
    print("Introduce cantidad a eliminar:")
    cantidadEliminar = int(input())
    encontrado = False
    for i in range(len(inventarioNombres)):
        if inventarioNombres[i] == productoEliminar:
            encontrado = True
            if inventarioCantidades[i] >= cantidadEliminar:
                inventarioCantidades[i] -= cantidadEliminar
            else:
                print("No hay suficiente stock")
            break
    if not encontrado:
        print("No existe el producto")
    else:
        print("Producto modificado correctamente")

def mostrar_inventario(inventarioCantidades, inventarioNombres):
    for i in range(len(inventarioNombres)):
        print(f"{inventarioNombres[i]} : {inventarioCantidades[i]}")
    print("**FIN_INVENTARIO**")

def ejecutar_inventario():
    op = 0
    while op != 4:
        try:
            print("\n--- MENÚ INVENTARIO ---")
            print("1) Añadir Stock\n2) Vender Producto\n3) Mostrar Inventario\n4) Salir")
            op = int(input("Seleccione una opción: "))
            match op:
                case 1:
                    añadir_stock(inventarioCantidades, inventarioNombres)
                case 2:
                    vender_producto(inventarioCantidades, inventarioNombres)
                case 3:
                    mostrar_inventario(inventarioCantidades, inventarioNombres)
                case 4:
                    print("PROGRAMA TERMINADO")
        except ValueError as e:
            print(f"Error: {e}")

ejecutar_inventario()