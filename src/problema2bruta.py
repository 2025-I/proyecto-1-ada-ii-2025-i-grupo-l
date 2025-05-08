from itertools import combinations

def obtener_relaciones(matriz):
    n = len(matriz)
    relaciones = {}
    for i in range(n):
        relaciones[i] = []
        for j in range(n):
            if matriz[i][j] == 1:
                relaciones[i].append(j)
    return relaciones

def es_valido(invitados, relaciones):
    invitados_set = set(invitados)
    for jefe in invitados:
        if jefe in relaciones:
            for subordinado in relaciones[jefe]:
                if subordinado in invitados_set:
                    return False
    return True

def fiestaFuerzaBruta(matriz, convivencias):
    n = len(matriz)
    relaciones = obtener_relaciones(matriz)
    mejor_convivencia = 0
    mejor_invitados = []

    for r in range(n + 1):
        for invitados in combinations(range(n), r):
            if es_valido(invitados, relaciones):
                suma = sum([convivencias[i] for i in invitados])
                if suma > mejor_convivencia:
                    mejor_convivencia = suma
                    mejor_invitados = list(invitados)

    # Crear la lista binaria de invitados
    binario_invitados = [1 if i in mejor_invitados else 0 for i in range(n)]

    return binario_invitados,mejor_convivencia

"""
n = 6
matriz = [
    [0, 1, 0, 0, 0,0],
    [0, 0, 1, 1, 0,0],
    [0, 0, 0, 0, 0,1],
    [0, 0, 0, 0, 1,0],
    [0, 0, 0, 0, 0,0],
    [0, 0, 0, 0, 0,0]
]
convivencias = [12, 18, 5, 10, 8,7]


print("Fuerza Bruta:", fiestaFuerzaBruta(matriz, convivencias))
"""