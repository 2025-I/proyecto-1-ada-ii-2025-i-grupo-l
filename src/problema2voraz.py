def fiesta_voraz(matriz, convivencias):
    n = len(matriz)
    seleccion = [0] * n
    no_disponibles = set()

    # Relaciones: hijos y padres por nodo
    hijos = {i: [] for i in range(n)}
    padres = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                hijos[i].append(j)
                padres[j].append(i)

    # Ordenar por mayor valor de convivencia
    nodos_ordenados = sorted(range(n), key=lambda x: convivencias[x], reverse=True)

    for nodo in nodos_ordenados:
        if nodo not in no_disponibles:
            seleccion[nodo] = 1
            no_disponibles.update(hijos[nodo])
            no_disponibles.update(padres[nodo])

    total = sum(convivencias[i] for i in range(n) if seleccion[i])
    
    return seleccion, total

