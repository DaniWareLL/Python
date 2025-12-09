import EjerciciosFunciones

EjerciciosFunciones.registrar_compra(
    "Daniel",
    "Libro", "Auriculares", "Café",
    metodo_pago="tarjeta",
    direccion="Calle Mayor 123",
    ciudad="Madrid",
    urgente=True
)

EjerciciosFunciones.calcular_precio(40, iva=21)

EjerciciosFunciones.tabla_multiplicar(5, hasta=12)

from EjerciciosFunciones import saludar

saludar()

from EjerciciosFunciones import make_pizza

print(make_pizza(8, "Tomate", "Queso", "Champiñón"))