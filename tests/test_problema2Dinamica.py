import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from problema2bruta import fiestaFuerzaBruta
from problema2dinamica import fiesta_programacion_dinamica




#TEST 1
def test_Dinamica_1():
    matriz = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    convivencias = [10, 30, 15, 5, 8]
    esperado_puntaje = 38
    binarios_validos = [[1, 0, 1, 0, 1], [0, 1, 0, 0, 1]]
    
    binario, puntaje = fiesta_programacion_dinamica(matriz, convivencias)
    assert puntaje == esperado_puntaje
    assert binario in binarios_validos
    

#TEST 2

def test_Dinamica_2():
    matriz = [
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0]
    ]
    convivencias = [10, 20, 25, 5, 15, 12]
    esperado_puntaje = 47
    binarios_validos = [[1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 1]]
    
    binario, puntaje = fiesta_programacion_dinamica(matriz, convivencias)
    assert puntaje == esperado_puntaje
    assert binario in binarios_validos



  
#TEST 3
def test_dinamica_3():
    n = 20
    # Crear árbol en cadena: 0 -> 1 -> 2 -> ... -> 99
    matriz = [[0]*n for _ in range(n)]
    for i in range(n - 1):
        matriz[i][i + 1] = 1

    # Convivencias entre 1 y 10
    convivencias = [i % 10 + 1 for i in range(n)]

    # Obtener resultados de ambas estrategias
    bin_bruta, puntaje_bruta = fiestaFuerzaBruta(matriz, convivencias)
    bin_dinamica, puntaje_dinamica = fiesta_programacion_dinamica(matriz, convivencias)

    # Comparar puntajes
    assert puntaje_bruta == puntaje_dinamica, (
        f"Puntaje diferente: Fuerza Bruta = {puntaje_bruta}, Dinámica = {puntaje_dinamica}"
    )

    # Verificación opcional: que ambos binarios tengan misma cantidad de invitados
    assert sum(bin_bruta) == sum(bin_dinamica), (
        "Cantidad de invitados diferente (aunque el puntaje sea igual)"
    )

   
#TEST 4
def test_dinamica_4():
    n = 25
    # Crear árbol en cadena: 0 -> 1 -> 2 -> ... -> 99
    matriz = [[0]*n for _ in range(n)]
    for i in range(n - 1):
        matriz[i][i + 1] = 1

    # Convivencias entre 1 y 10
    convivencias = [i % 10 + 1 for i in range(n)]

    # Obtener resultados de ambas estrategias
    bin_bruta, puntaje_bruta = fiestaFuerzaBruta(matriz, convivencias)
    bin_dinamica, puntaje_dinamica = fiesta_programacion_dinamica(matriz, convivencias)

    # Comparar puntajes
    assert puntaje_bruta == puntaje_dinamica, (
        f"Puntaje diferente: Fuerza Bruta = {puntaje_bruta}, Dinámica = {puntaje_dinamica}"
    )

    # Verificación opcional: que ambos binarios tengan misma cantidad de invitados
    assert sum(bin_bruta) == sum(bin_dinamica), (
        "Cantidad de invitados diferente (aunque el puntaje sea igual)"
    )
