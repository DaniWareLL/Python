#EJERCICIO1
def info_argumentos(*args):
    contador : int = 0
    print("Argumentos: ")
    for arg in args:
        print(arg)
        contador += 1
    print("Contador: "+str(contador))

def divisibles3(*args):
    for arg in args:
        if arg % 3 == 0:
            print(arg)

def histograma(*args):
    for arg in args:
        for i in range(arg):
            print("*")

#EJERCICIO2
def coste_envio (tarifa_base: int = 5, *, peso : int, urgente = False):


    resultado : float
    if peso == 1:
        resultado = tarifa_base
    else :
        resultado = tarifa_base + (2 * (peso -1))

    if urgente:
        resultado = resultado * 1.3

    return resultado

#EJERCICIO3
def convertir_segundos (horas, minutos, segundos):
    return ( horas * 60 * 60 ) + ( minutos * 60 ) + segundos