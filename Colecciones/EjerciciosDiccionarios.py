# Ejercicio1

monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa = input("Introduzca una divisa: ")
if divisa in monedas:
    print(monedas[divisa])

# Ejercicio2
nombre = input('Introduzca nombre:')
edad = input('Introduzca edad:')
direccion = input('Introduzca direccion:')
telefono = input('Introduzca telefono:')

temp = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(temp['nombre'], 'tiene', temp['edad'], 'años, vive en', temp['direccion'], 'y su número de teléfono es',
      temp['telefono'])

#Ejercicio3
frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('Escoge una fruta')
kg = float(input('Introduce los KG'))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')

#Ejercicio4
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])

#Ejercicio5
curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total= 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total += creditos
print('Total: ', total)

#Ejercicio6
persona = {}
continuar = True
while continuar:
    clave = input('Introduce datos: ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('Introduce Si, si quiere continuar introduciendo información o No') == "Si"

#Ejercicio7
cesta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio: '))
    cesta[item] = precio
    continuar = input('¿Quiere seguir introduciendo articulos?') == "Si"
coste = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)

#Ejercicio8
frase = input("Introduzca una frase: <palabra>:<traducción>, <palabra>:<traducción>")

for item in frase.split(","):
    clave, valor = item.split(":")