#1
print("¿Cuanto quieres invertir?")
inversion = int(input())
print("Indique el interes anual: ")
interes = float(input())
print("¿Durante cuantos años?")
años = int(input())

for i in range(años):
    inversion += (inversion * (interes/100))
print (inversion)

#2
print("Introduce un numero positivo: ")
numero = int(input())
for i in range(numero, 0, -1):
    print(i,",", end="")

#3
for i in range(80, 200):
    if i % 7 == 0:
        print(i)
        break
#4

inventarioCantidades  = []
inventarioNombres = []
op : int = 0

while op != 4:
    try:
        print("1) Añadir Stock\n"
              "2) Vender Producto\n"
              "3) Mostrar Inventario\n"
              "4) Salir")
        op = int(input())
        match op :
            case 1:
                try:
                    print("Introduzca cantidad: ")
                    cantidad = int(input())
                    inventarioCantidades.append(cantidad)
                    print("Introduzca producto: ")
                    producto = input()
                    inventarioNombres.append(producto)
                except ValueError:
                    print("Introduce un numero positivo")
            case 2:
                print("Introduce el tipo de producto a borra: ")
                productoEliminar = input()
                print("Introduce cantidad a eliminar: ")
                cantidadEliminar = int(input())
                for i in inventarioNombres:
                    if inventarioNombres == productoEliminar:
                        inventarioNombres[i] - cantidadEliminar
                    else:
                        print("No existe el producto")
            case 3:
                for i in range(len(inventarioNombres)):
                    print(inventarioNombres[i]," : ",inventarioCantidades[i])
                print("**FIN_INVENTARIO**")
            case 4:
                print("PROGRAMA TERMINADO")
                break
    except ValueError as e:
        print(f"Error: {e}")