def calcular_pago(horas, tarifa):
    if horas <= 40:
        pago = horas * tarifa
    else:
        horas_extra = horas - 40
        pago = (40 * tarifa) + (horas_extra * tarifa * 1.5)
    return pago

def solicitar_datos_y_calcular():
    entrada_horas = input("Introduce las horas trabajadas: ")
    entrada_tarifa = input("Introduce la tarifa por hora: ")
    horas = float(entrada_horas)
    tarifa = float(entrada_tarifa)
    pago_total = calcular_pago(horas, tarifa)
    print("Pago bruto:", pago_total)

# Ejecutar el programa
solicitar_datos_y_calcular()