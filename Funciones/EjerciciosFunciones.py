# 1)
def saludar(*, nombre: str, saludo: str = "Hola"):
    return saludo + " " + nombre

# 2)
def calcular_precio(precio_base: float, *, iva: float = 21):
    precio_final = precio_base * (1 + iva / 100)
    return precio_final

# 3)
def crear_usuario(*, nombre: str, email: str, activo: bool = True):
    if activo:
        return [nombre, email, activo]
    return []

# 4)
def formatear_nombre(nombre: str, apellido: str, *, orden: str = "nombre_apellido"):
    if orden == "apellido_nombre":
        return apellido + " " + nombre
    return nombre + " " + apellido

# 5)
def calcular_descuento(precio_original: float, *, descuento: float = 10):
    precio_final = precio_original * (1 - descuento / 100)
    return precio_final

# 7)
def filtrar_pares(numeros: list[int]):
    pares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares

# 8)
def tabla_multiplicar(numero: int, *, hasta: int = 10):
    tabla = []
    for i in range(1, hasta + 1):
        tabla.append(f"{numero} x {i} = {numero * i}")
    return tabla

# Ejercicio inventado Daniel Lillo

def registrar_compra(cliente, *productos, metodo_pago="efectivo", **detalles_envio):
    print(f"Cliente: {cliente}")
    print("Productos comprados:")
    for producto in productos:
        print(f" - {producto}")
    print(f"Método de pago: {metodo_pago}")

    if detalles_envio:
        print("Detalles de envío:")
        for clave, valor in detalles_envio.items():
            print(f" {clave}: {valor}")

registrar_compra(
    "Daniel",
    "Libro", "Auriculares", "Café",
    metodo_pago="tarjeta",
    direccion="Calle Mayor 123",
    ciudad="Madrid",
    urgente=True
)

def make_pizza (tamano, * ingredientes):
    print("Ingredientes: ")
    for ingrediente in ingredientes:
        print(f" - {ingrediente}")
    print ("El tamaño en 8 porciones es: ", tamano / 8)

def calcularFactorial (numero: int):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def fibonacci (numero: int):
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    return fibonacci(numero - 1) + fibonacci(numero - 2)