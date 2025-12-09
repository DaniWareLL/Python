# Ejercicio 1: Verificación de número primo con control de errores
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

# Ejercicio 2: Conversor de divisas con control de errores
try:
    cantidad = float(input("Introduce la cantidad en euros: "))

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva.")

    divisa = input("Introduce la divisa destino (USD, GBP, JPY): ").upper()

    match divisa:
        case "USD":
            tasa = 1.06
        case "GBP":
            tasa = 0.87
        case "JPY":
            tasa = 157.12
        case _:
            raise ValueError("Divisa no válida.")

    convertido = cantidad * tasa
    print(f"{cantidad} EUR son {convertido:.2f} {divisa}")

except ValueError as e:
    print(f"Error: {e}")

# Ejercicio 3: Cálculo de raíces reales de una ecuación cuadrática
try:
    a = float(input("Introduce el coeficiente a: "))
    b = float(input("Introduce el coeficiente b: "))
    c = float(input("Introduce el coeficiente c: "))
    if a == 0:
        raise ValueError("a no puede ser cero.")
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        raise ValueError("No hay raíces reales (discriminante negativo).")
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print(f"Las raíces reales son: x1 = {x1:.2f}, x2 = {x2:.2f}")
except ValueError as e:
    print(f"Error: {e}")

# Ejercicio 4: Simulador de cajero automático
try:
    saldo = float(input("Introduce el saldo inicial: "))
    retiro = float(input("Introduce la cantidad a retirar: "))
    if saldo < 0 or retiro < 0:
        raise ValueError("El saldo y la cantidad deben ser positivos.")
    if retiro > saldo:
        raise ValueError("Fondos insuficientes.")
    saldo_restante = saldo - retiro
    print(f"Retiro exitoso. Saldo restante: {saldo_restante:.2f} EUR")
except ValueError as e:
    print(f"Error: {e}")

# Ejercicio 5: Calculadora de operaciones con manejo múltiple de excepciones
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operacion = input("Introduce la operación (+, -, *, /): ")
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        resultado = num1 / num2
    else:
        raise ValueError("Operación no reconocida.")
    print(f"Resultado: {resultado}")
except ValueError as ve:
    print(f"Error de valor: {ve}")
except ZeroDivisionError as zde:
    print(f"Error matemático: {zde}")
except Exception as e:
    print(f"Error inesperado: {e}")