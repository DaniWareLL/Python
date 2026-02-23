
def traducir (frase):
    diccionario = "hola:hello, adiós:goodbye, casa:house, perro:dog, gato:cat, mesa:table, silla:chair, coche:car, libro:book, escuela:school, niño:child, mujer:woman, hombre:man, comida:food, agua:water, pan:bread, leche:milk, fruta:fruit, carne:meat, pescado:fish, yo:I, tú:you, él:he, ella:she, nosotros:we, ellos:they, mi:my, tu:your, su:his, nuestra:our, el:the, la:the, los:the, las:the, un:a, una:a, en:in, con:with, sin:without, para:for, por:by, sobre:on, entre:between, desde:from, hasta:until, grande:big, pequeño:small, nuevo:new, viejo:old, bueno:good, malo:bad, rápido:fast, lento:slow, siempre:always, nunca:never, hoy:today, mañana:tomorrow, ayer:yesterday, comer:eat, beber:drink, correr:run, caminar:walk, hablar:speak, escribir:write, leer:read, dormir:sleep, vivir:live, amar:love, ver:see, escuchar:listen, pensar:think, saber:know, querer:want, poder:can, trabajar:work, estudiar:study, jugar:play, abrir:open, cerrar:close, rojo:red, azul:blue, verde:green, amarillo:yellow, blanco:white, negro:black, gracias:thanks, sí:yes, no:no"
    diccionario_format = {}
    traduccion = []

    for palabra in diccionario.split(","):
        clave_valor = palabra.split(":")
        clave = clave_valor[0].strip()
        valor = clave_valor[1].strip()
        diccionario_format[clave] = valor

    print(diccionario_format)

    for palabra in frase:
        if palabra in diccionario_format:
            traduccion.append(diccionario_format[palabra])
    print(traduccion)


traducir(["hola", "adiós", "casa", "gato"])
