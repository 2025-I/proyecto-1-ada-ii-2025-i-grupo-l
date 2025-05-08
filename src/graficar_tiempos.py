import time
import matplotlib.pyplot as plt
from problema2bruta import fiestaFuerzaBruta
from problema2dinamica import fiesta_programacion_dinamica
from problema2voraz import fiesta_voraz

# Generar una matriz jerárquica en cadena de 25x25
def generar_matriz_25():
    n = 25
    matriz = [[0]*n for _ in range(n)]
    for i in range(n - 1):
        matriz[i][i + 1] = 1
    convivencias = [i % 10 + 1 for i in range(n)]
    return matriz, convivencias

# Medir tiempos de ejecución
def medir_tiempos():
    matriz, convivencias = generar_matriz_25()
    tiempos = {}

    inicio = time.perf_counter()
    fiestaFuerzaBruta(matriz, convivencias)
    tiempos["Fuerza Bruta"] = time.perf_counter() - inicio

    inicio = time.perf_counter()
    fiesta_programacion_dinamica(matriz, convivencias)
    tiempos["Programación Dinámica"] = time.perf_counter() - inicio

    inicio = time.perf_counter()
    fiesta_voraz(matriz, convivencias)
    tiempos["Voraz"] = time.perf_counter() - inicio

    return tiempos

# Graficar los tiempos
def graficar(tiempos):
    estrategias = list(tiempos.keys())
    valores = list(tiempos.values())

    plt.figure(figsize=(8,5))
    plt.bar(estrategias, valores, color=["red", "green", "blue"])
    plt.title("Tiempos de ejecución (n = 25)")
    plt.ylabel("Tiempo (segundos)")
    plt.xlabel("Estrategia")
    plt.tight_layout()
    plt.savefig("docs/imagenes/tiempos_25.png")  # Guarda la imagen
    plt.show()

# Ejecutar
if __name__ == "__main__":
    tiempos = medir_tiempos()
    print("Tiempos medidos:", tiempos)
    graficar(tiempos)
