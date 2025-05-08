import re  # Biblioteca para expresiones regulares, usada en la normalización de cadenas.
import unicodedata  # Biblioteca para manejar caracteres Unicode y eliminar acentos.
from problema1bruta import subsecuencia_palindromica_bruta  # Importa el método de Fuerza Bruta.
from problema1dinamica import subsecuencia_palindromica_dinamica  # Importa el método de Programación Dinámica.
from problema1voraz import subsecuencia_palindromica_voraz  # Importa el método de Manacher (Voraz).

# =========================================
# FUNCIÓN DE NORMALIZACIÓN DE LA CADENA
# =========================================
def normalizar_cadena(cadena: str) -> str:

    # Descompone caracteres para eliminar acentos.
    cadena = ''.join(
        c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'
    )

    # Filtra caracteres no alfanuméricos y convierte la cadena a minúsculas.
    return ''.join(re.findall(r'[a-zA-Z0-9]', cadena)).lower()


# FUNCIÓN PARA ENCONTRAR PALÍNDROMOS
def encontrar_palindromos(s: str) -> dict:
 
    return {
        "bruta": subsecuencia_palindromica_bruta(s),  # Método de Fuerza Bruta.
        "dinámica": subsecuencia_palindromica_dinamica(s),  # Método de Programación Dinámica.
        "voraz": subsecuencia_palindromica_voraz(s)  # Método de Manacher.
    }