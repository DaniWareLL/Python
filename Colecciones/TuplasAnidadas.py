estudiantes = (
    ("Ana",
        ("Matemáticas", 9),
        ("Historia", 2),
        ("Programación", 10)
    ),
    ("Luis",
        ("Matemáticas", 6),
        ("Historia", 1),
        ("Programación", 9)
    ),
    ("María",
        ("Matemáticas", 10),
        ("Historia", 9),
        ("Programación", 10)
    )
)

for nombre, asig1, asig2, nota in estudiantes:
    print(nombre)
    print(asig1[0], asig1[1])
    print(asig2[0], asig2[1])

print("****FILTRO CONCRETO****")
print(estudiantes[0][3][1])  # 10