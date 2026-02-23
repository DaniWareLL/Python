def cuentaVocales(cadena):
    contadorA, contadorE, contadorI, contadorO, contadorU = 0, 0, 0, 0, 0

    cadena = cadena.lower()

    for c in cadena:
        if c == "a":
            contadorA += 1
        if c == "e":
            contadorE += 1
        if c == "i":
            contadorI += 1
        if c == "o":
            contadorO += 1
        if c == "u":
            contadorU += 1

    print("La vocal a aparece " + str(contadorA) + " vez")
    print("La vocal e aparece " + str(contadorE) + " vez")
    print("La vocal i aparece " + str(contadorI) + " vez")
    print("La vocal o aparece " + str(contadorO) + " vez")
    print("La vocal u aparece " + str(contadorU) + " vez")

cuentaVocales("me duele el estemocleidomastoideo")
