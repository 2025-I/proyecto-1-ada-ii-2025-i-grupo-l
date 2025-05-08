# matrices_para_tests.py

def generar_matriz_cadena(n=1000):
    matriz = [[0]*n for _ in range(n)]
    for i in range(n - 1):
        matriz[i][i + 1] = 1  # nodo i es jefe de i+1
    convivencias = [i % 10 + 1 for i in range(n)]  # valores entre 1 y 10
    return matriz, convivencias

# Exportamos una matriz grande válida
matriz_grande_1000, convivencias_grande_1000 = generar_matriz_cadena()

print(matriz_grande_1000)