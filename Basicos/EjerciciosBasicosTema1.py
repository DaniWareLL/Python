#1
try:
    print("Introduzca su edad: ")
    edad : int = int(input())
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
except ValueError as e:
    print("Error: ",e)

#2
try:
    print("Introduce el primer numero: ")
    num1 = int(input())
    print("Introduce el segundo numero: ")
    num2 = int(input())
    if num1 > num2:
        print( num1," es mayor que ", num2)
    else :
        print( num2," es mayor que ", num1)
except ValueError as e:
    print("Error: ",e)


#3
try:
    print("Escribe una nota de examen: ")
    nota = float(input())
    if nota > 0 and nota < 5:
        print("SUSPENSO")
    elif nota > 5 and nota < 7:
        print("APROBADO")
    elif nota > 7 and nota < 9:
        print("NOTABLE")
    elif nota > 9 and nota < 11:
        print("SOBRESALIENTE")
    else :
        print("ERROR, Untroduce una nota valida")
except ValueError as e:
    print("Error: ",e)

#4
print("Introduce la clave python123")
clave = input()
if clave == "python123":
    print("CORRECTO")
else:
    print("ERROR")