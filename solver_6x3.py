from datetime import date, timedelta

OPERADORES = list("ABCDEFGHIJKL")

PATRON_VERANO = [
    "M", "M",
    "T", "T",
    "N", "N",
    "4", "4", "4", "4"
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

        turno = PATRON_VERANO[
            (dia + offset) % len(PATRON_VERANO)
        ]

        cuadrante[(op, fecha)] = turno

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

        turno = cuadrante[(op, fecha)]

        if turno == "M":
            m += 1
        elif turno == "T":
            t += 1
        elif turno == "N":
            n += 1

    print(
        fecha,
        "M=", m,
        "T=", t,
        "N=", n
    )

    fecha += timedelta(days=1)

print("FIN")