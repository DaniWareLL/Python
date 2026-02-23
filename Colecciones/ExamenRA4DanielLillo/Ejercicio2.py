elementos = [1, 2, 2, 4, 5, 1, 1, 9, 8, 1]

def calcularPosicion(n, datos):
    posiciones = []
    for i, num in enumerate(datos):
        if num == n:
            posiciones.append(i + 1)  # +1 si quieres posiciones desde 1

    if len(posiciones) == 0:
        return -1
    else:
        return posiciones

print(calcularPosicion(6, elementos))   #-1 (no esta)
print(calcularPosicion(9, elementos))   #Posicion 8
print(calcularPosicion(1, elementos))


def calcularPosicionAñade(n, datos):
    posiciones = []
    encontrado = False
    for i, num in enumerate(datos):
        if num == n:
            encontrado = True
            posiciones[i] = n
    if not encontrado:
        posiciones.append(n)
    else:
        return posiciones

    if len(posiciones) == 0:
        datos.append(n)
        print(datos)

calcularPosicionAñade(6, elementos) #Añade 6