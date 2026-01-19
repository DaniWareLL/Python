# Ejercicio1
usuarios = ["Marta", "David", "Elvira", "Juan", "Marcos"]
administradores = [usuarios[0], usuarios[3]]
administradores.remove("Juan")
administradores.append("Marcos")

for u in usuarios:
    if u in administradores:
        print(u+ " es admin")
    else:
        print(u+ " no es admin")