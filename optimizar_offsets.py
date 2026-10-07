from datetime import date, timedelta

OPERADORES = list("ABCDEFGHIJKL")

PATRON = [
    "M", "M",
    "T", "T",
    "N", "N",
    "4", "4", "4"
]

INICIO = date(2027, 6, 1)
FIN = date(2027, 6, 30)

MEJOR_SCORE = 999999
MEJORES_OFFSETS = None

def evaluar(offsets):

    fecha = INICIO

    score = 0

    while fecha <= FIN:

        m = 0
        t = 0
        n = 0

        dia = (fecha - INICIO).days

        for op in OPERADORES:

            turno = PATRON[
                (dia + offsets[op]) % len(PATRON)
            ]

            if turno == "M":
                m += 1

            elif turno == "T":
                t += 1

            elif turno == "N":
                n += 1

        # penalizar déficits

        if m < 2:
            score += 1000

        if t < 2:
            score += 1000

        if n < 2:
            score += 1000

        # penalizar exceso de noches

        if n > 2:
            score += (n - 2) * 10

        fecha += timedelta(days=1)

    return score


# búsqueda simple

offsets = {}

for i, op in enumerate(OPERADORES):

    offsets[op] = i % 9

MEJOR_SCORE = evaluar(offsets)
MEJORES_OFFSETS = offsets.copy()

print()
print("OFFSETS INICIALES")
print(MEJORES_OFFSETS)
print("SCORE =", MEJOR_SCORE)

# optimización local

mejora = True

while mejora:

    mejora = False

    for op in OPERADORES:

        actual = MEJORES_OFFSETS[op]

        for nuevo in range(9):

            temp = MEJORES_OFFSETS.copy()

            temp[op] = nuevo

            score = evaluar(temp)

            if score < MEJOR_SCORE:

                MEJOR_SCORE = score
                MEJORES_OFFSETS = temp

                mejora = True

print()
print("MEJOR SOLUCION")
print("--------------")

for op in OPERADORES:

    print(
        op,
        MEJORES_OFFSETS[op]
    )

print()
print("SCORE FINAL =", MEJOR_SCORE)