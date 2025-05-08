from problema2bruta import fiestaFuerzaBruta
from problema2dinamica import fiesta_programacion_dinamica
from problema2voraz import fiesta_voraz




def resolver_fiesta(matriz, convivencias):
    return {
        "bruta": fiestaFuerzaBruta(matriz, convivencias),
        "dinámica": fiesta_programacion_dinamica(matriz, convivencias),
        "voraz": fiesta_voraz(matriz, convivencias)
    }
    
