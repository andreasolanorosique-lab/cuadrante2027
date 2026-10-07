from datetime import date, timedelta

OPERADORES = 12

PATRONES = {
    "6x3": [
        "M","M",
        "T","T",
        "N","N",
        "4","4","4"
    ],

    "6x4": [
        "M","M",
        "T","T",
        "N","N",
        "4","4","4","4"
    ],

    "6x5": [
        "M","M",
        "T","T",
        "N","N",
        "4","4","4","4","4"
    ]
}

INICIO = date(2027, 6, 1)
FIN = date(2027, 6, 30)

for nombre, patron in PATRONES.items():

    print()
    print("=" * 50)
    print("PATRON", nombre)
    print("=" * 50)

    minimo_m = 999
    minimo_t = 999
    minimo_n = 999

    maximo_m = 0
    maximo_t = 0
    maximo_n = 0

    deficit = 0
    exceso_noches = 0

    fecha = INICIO

    while fecha <= FIN:

        dia_indice = (fecha - INICIO).days

        m = 0
        t = 0
        n = 0

        for op in range(OPERADORES):

            offset = op % len(patron)

            turno = patron[
                (dia_indice + offset)
                % len(patron)
            ]

            if turno == "M":
                m += 1

            elif turno == "T":
                t += 1

            elif turno == "N":
                n += 1

        minimo_m = min(minimo_m, m)
        minimo_t = min(minimo_t, t)
        minimo_n = min(minimo_n, n)

        maximo_m = max(maximo_m, m)
        maximo_t = max(maximo_t, t)
        maximo_n = max(maximo_n, n)

        if m < 2 or t < 2 or n < 2:
            deficit += 1

        if n > 2:
            exceso_noches += 1

        fecha += timedelta(days=1)

    print("Min M:", minimo_m)
    print("Max M:", maximo_m)

    print("Min T:", minimo_t)
    print("Max T:", maximo_t)

    print("Min N:", minimo_n)
    print("Max N:", maximo_n)

    print("Dias con deficit:", deficit)
    print("Dias con exceso de noches:", exceso_noches)