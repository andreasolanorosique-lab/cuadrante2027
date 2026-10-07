from datetime import date, timedelta

OPERADORES = list("ABCDEFGHIJKL")

VACACIONES = {
    "A": [
        (date(2027, 6, 1), date(2027, 6, 15)),
        (date(2027, 8, 1), date(2027, 8, 15))
    ],

    "B": [
        (date(2027, 6, 1), date(2027, 6, 15)),
        (date(2027, 8, 16), date(2027, 8, 31))
    ],

    "C": [
        (date(2027, 6, 1), date(2027, 6, 15)),
        (date(2027, 9, 1), date(2027, 9, 15))
    ],

    "D": [
        (date(2027, 6, 16), date(2027, 6, 30)),
        (date(2027, 8, 1), date(2027, 8, 15))
    ],

    "E": [
        (date(2027, 6, 16), date(2027, 6, 30)),
        (date(2027, 8, 16), date(2027, 8, 31))
    ],

    "F": [
        (date(2027, 6, 16), date(2027, 6, 30)),
        (date(2027, 9, 1), date(2027, 9, 15))
    ],

    "G": [
        (date(2027, 7, 1), date(2027, 7, 15)),
        (date(2027, 8, 1), date(2027, 8, 15))
    ],

    "H": [
        (date(2027, 7, 1), date(2027, 7, 15)),
        (date(2027, 8, 16), date(2027, 8, 31))
    ],

    "I": [
        (date(2027, 7, 1), date(2027, 7, 15)),
        (date(2027, 9, 1), date(2027, 9, 15))
    ],

    "J": [
        (date(2027, 7, 16), date(2027, 7, 31)),
        (date(2027, 9, 16), date(2027, 9, 30))
    ],

    "K": [
        (date(2027, 7, 16), date(2027, 7, 31)),
        (date(2027, 9, 16), date(2027, 9, 30))
    ],

    "L": [
        (date(2027, 7, 16), date(2027, 7, 31)),
        (date(2027, 8, 1), date(2027, 8, 15))
    ]
}
def esta_de_vacaciones(op, fecha):

    if op not in VACACIONES:
        return False

    for inicio, fin in VACACIONES[op]:

        if inicio <= fecha <= fin:
            return True

    return False

PATRON_VERANO = [
    "M", "M",
    "T", "T",
    "N", "N",
    "4", "4", "4"
]

OFFSETS = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 0,
    "K": 1,
    "L": 2
}

INICIO = date(2027, 6, 1)
FIN = date(2027, 6, 30)

cuadrante = {}

for op in OPERADORES:
    
    offset = OFFSETS[op]

    fecha = INICIO
    dia = 0

    while fecha <= FIN:

        if esta_de_vacaciones(op, fecha):

            turno = "V"

    else:

        turno = PATRON_VERANO[
    (dia + offset) % len(PATRON_VERANO)
]
turno = PATRON_VERANO[
    (dia + offset) % len(PATRON_VERANO)
]

if esta_de_vacaciones(op, fecha):
    turno = "V"

fecha += timedelta(days=1)
dia += 1

print("COBERTURA JUNIO")
print("----------------")

fecha = INICIO

while fecha <= FIN:

    m = 0
    t = 0
    n = 0

    for op in OPERADORES:

        if turno == "V":
            continue

        turno = cuadrante[(op, fecha)]

        if turno == "M":
            m += 1

        elif turno == "T":
            t += 1

        elif turno == "N":
            n += 1

    # <- EL PRINT VA AQUÍ

    print(
        fecha,
        "M=", m,
        "T=", t,
        "N=", n
    )

    if m < 2 or t < 2 or n < 2:

        print("FALLO COBERTURA")

    fecha += timedelta(days=1)