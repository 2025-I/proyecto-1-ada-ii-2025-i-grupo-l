import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from problema2bruta import fiestaFuerzaBruta





#TEST 1
def test_bruta_caso_manual_1():
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
    
    binario, puntaje = fiestaFuerzaBruta(matriz, convivencias)
    assert puntaje == esperado_puntaje
    assert binario in binarios_validos
    

#TEST 2

def test_bruta_caso_manual_2():
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
    
    binario, puntaje = fiestaFuerzaBruta(matriz, convivencias)
    assert puntaje == esperado_puntaje
    assert binario in binarios_validos

   

