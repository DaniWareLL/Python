#EJERCICIO1
lista1 = ["Infanta", "Jose", "Juan"]
lista2 = ["Elena", "Javier", "Juan"]
contador = 0

for i in lista1:
    for j in lista2:
        try:
            if i != j:
                contador += 1
                print(i,j)
                if i == "Infanta" and j == "Elena":
                     raise Exception
            else:
                print(j, "y", i, "son iguales y no se pueden mezclar")
        except Exception:
            print("IES en Galapagar con estudios de formacion profesional")
print("El numero de combinaciones hechas ha sido: ", contador)


#EJERCICIO2
preciosProductos : float = 0
contador = 0
acumulador = 0
max : float = preciosProductos

while preciosProductos != 9999.99:
    preciosProductos = float(input("Ingrese el precio del producto: "))
    if preciosProductos == 9999.99:
        break
    else:
        try:
            if preciosProductos < 0:
                raise ValueError
            else :
                if preciosProductos >= 10 :
                    if preciosProductos > max:
                        max = preciosProductos
                        acumulador += preciosProductos
                        contador += 1
                        print(preciosProductos)
        except ValueError:
            print("ERROR")

print("Se ha cumplido esa condicion: ",contador)

try:
    print("El precio medio ha sido: ", acumulador/contador)
except ZeroDivisionError:
    print("ERROR, no se puede dividir por 0, por lo que el precio medio es 0")

print("El precio mas alto ha sido: ", max)

#EJERCICIO3
a = 0
b = 1
for i in range(0,10):
    print(a, end=" ")
    a, b = b, a + b