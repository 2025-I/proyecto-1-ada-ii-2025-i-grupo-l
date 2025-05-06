import re
from problema1bruta import subsecuencia_palindromica_bruta
from problema1dinamica import subsecuencia_palindromica_dinamica
from problema1voraz import subsecuencia_palindromica_voraz

def normalizar_cadena(cadena: str) -> str:
    """Normaliza la cadena eliminando caracteres no alfanuméricos y convirtiendo a minúsculas."""
    return ''.join(re.findall(r'[a-zA-Z0-9]', cadena)).lower()

def encontrar_palindromos(s: str) -> dict:
    """Ejecuta las tres estrategias y devuelve los resultados en un diccionario."""
    return {
        "bruta": subsecuencia_palindromica_bruta(s),
        "dinámica": subsecuencia_palindromica_dinamica(s),
        "voraz": subsecuencia_palindromica_voraz(s)
    }