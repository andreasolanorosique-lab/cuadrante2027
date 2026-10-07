from ortools.sat.python import cp_model

OPERADORES = list("ABCDEFGHIJKL")

PATRON = [
    1, 1,   # MM
    2, 2,   # TT
    3, 3,   # NN
    0, 0, 0, 0, 0, 0  # 444444
]

DIAS = 365
LONGITUD = len(PATRON)

model = cp_model.CpModel()

offset = {}

for op in OPERADORES:
    offset[op] = model.NewIntVar(
        0,
        LONGITUD - 1,
        f"offset_{op}"
    )

turno = {}

for op in OPERADORES:

    for d in range(DIAS):

        turno[op, d] = model.NewIntVar(
            0,
            3,
            f"{op}_{d}"
        )

        opciones = []

        for k in range(LONGITUD):

            b = model.NewBoolVar(
                f"{op}_{d}_{k}"
            )

            model.Add(
                offset[op] == k
            ).OnlyEnforceIf(b)

            model.Add(
                offset[op] != k
            ).OnlyEnforceIf(b.Not())

            model.Add(
                turno[op, d]
                ==
                PATRON[(d + k) % LONGITUD]
            ).OnlyEnforceIf(b)

            opciones.append(b)

        model.AddExactlyOne(opciones)

for d in range(DIAS):

    m = []
    t = []
    n = []

    for op in OPERADORES:

        es_m = model.NewBoolVar(
            f"m_{op}_{d}"
        )

        es_t = model.NewBoolVar(
            f"t_{op}_{d}"
        )

        es_n = model.NewBoolVar(
            f"n_{op}_{d}"
        )

        model.Add(
            turno[op, d] == 1
        ).OnlyEnforceIf(es_m)

        model.Add(
            turno[op, d] != 1
        ).OnlyEnforceIf(es_m.Not())

        model.Add(
            turno[op, d] == 2
        ).OnlyEnforceIf(es_t)

        model.Add(
            turno[op, d] != 2
        ).OnlyEnforceIf(es_t.Not())

        model.Add(
            turno[op, d] == 3
        ).OnlyEnforceIf(es_n)

        model.Add(
            turno[op, d] != 3
        ).OnlyEnforceIf(es_n.Not())

        m.append(es_m)
        t.append(es_t)
        n.append(es_n)

    model.Add(sum(m) >= 2)
    model.Add(sum(t) >= 2)
    model.Add(sum(n) >= 2)

solver = cp_model.CpSolver()

solver.parameters.max_time_in_seconds = 60

status = solver.Solve(model)

print()
print("STATUS =", solver.StatusName(status))
print()

print("OFFSETS")
print("-------")

for op in OPERADORES:

    print(
        op,
        solver.Value(offset[op])
    )
print()
print("COBERTURA")
print("---------")

for d in range(DIAS):

    m = 0
    t = 0
    n = 0

    for op in OPERADORES:

        valor = solver.Value(
            turno[op, d]
        )

        if valor == 1:
            m += 1

        elif valor == 2:
            t += 1

        elif valor == 3:
            n += 1

    print(
        f"Dia {d+1:03d}",
        f"M={m}",
        f"T={t}",
        f"N={n}"
    )