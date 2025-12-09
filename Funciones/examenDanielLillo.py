import operaciones


#PRUEBAS EJERCICIO1

print("+++++1)+++++")
operaciones.info_argumentos(1,2,3,4,5)

print("+++++2)+++++")
operaciones.divisibles3(1,2,3,4,5,6)

print("+++++3)+++++")
operaciones.histograma(4, 9, 7)



#PRUEBAS EJERCICIO2
print("+++++4)+++++")
resultadoFuncion = operaciones.coste_envio(2, peso = 3, urgente = False)
print(resultadoFuncion)



#PRUEBAS EJERCICIO3
print("+++++5)+++++")
print("Introduce las horas: ")
horas : int = int(input())

print("Introduce las minutos: ")
minutos : int = int(input())

print("Introduce las segundos: ")
segundos : int = int(input())

if horas > 0 and minutos > 0 and segundos > 0:
    if horas <= 24 and minutos < 60 and segundos < 60:
        resultado = operaciones.convertir_segundos(horas, minutos, segundos)
        print(resultado)
    else:
        print("Horas no puede ser mayor de 24 y minutos y segundos no pueden ser mayores de 60")
else :
    print("Ningun valor puede ser negativo")