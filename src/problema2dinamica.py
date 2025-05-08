from collections import defaultdict

# Construir jerarquía
def construir_arbol(matriz):
    n = len(matriz)
    hijos = defaultdict(list)
    es_hijo = [False] * n

    for padre in range(n):
        for hijo in range(n):
            if matriz[padre][hijo] == 1:
                hijos[padre].append(hijo)
                es_hijo[hijo] = True

    raiz = es_hijo.index(False)
    return hijos, raiz

# Programación dinámica sobre árbol
def dp_fiesta(nodo, hijos, convivencias, dp):
    if nodo in dp:
        return dp[nodo]

    # Caso 1: incluir nodo actual
    incluir_total = convivencias[nodo]
    incluir_seleccion = [0] * len(convivencias)
    incluir_seleccion[nodo] = 1  # este nodo va

    for h in hijos[nodo]:
        _, excl_sel, excl_val = dp_fiesta(h, hijos, convivencias, dp)
        incluir_total += excl_val
        for i in range(len(convivencias)):
            incluir_seleccion[i] |= excl_sel[i]

    # Caso 2: excluir nodo actual
    excluir_total = 0
    excluir_seleccion = [0] * len(convivencias)

    for h in hijos[nodo]:
        inc_sel, exc_sel, inc_val = dp_fiesta(h, hijos, convivencias, dp)
        inc_val_alt = sum(convivencias[i] for i in range(len(inc_sel)) if inc_sel[i])
        exc_val_alt = sum(convivencias[i] for i in range(len(exc_sel)) if exc_sel[i])
        if inc_val_alt > exc_val_alt:
            excluir_total += inc_val_alt
            for i in range(len(convivencias)):
                excluir_seleccion[i] |= inc_sel[i]
        else:
            excluir_total += exc_val_alt
            for i in range(len(convivencias)):
                excluir_seleccion[i] |= exc_sel[i]

    dp[nodo] = (
        incluir_seleccion,
        excluir_seleccion,
        incluir_total if incluir_total > excluir_total else excluir_total
    )

    return dp[nodo]

# Función principal
def fiesta_programacion_dinamica(matriz, convivencias):
    hijos, raiz = construir_arbol(matriz)
    dp = {}
    inc_sel, exc_sel, _ = dp_fiesta(raiz, hijos, convivencias, dp)

    total_inc = sum(convivencias[i] for i in range(len(inc_sel)) if inc_sel[i])
    total_exc = sum(convivencias[i] for i in range(len(exc_sel)) if exc_sel[i])

    if total_inc > total_exc:
        seleccion = inc_sel
        total = total_inc
    else:
        seleccion = exc_sel
        total = total_exc

    
    return  seleccion,total


