def subsecuencia_palindromica_voraz(s: str) -> str:
    """Encuentra la subcadena palindrómica más larga usando un enfoque voraz (expansión desde el centro)."""
    def expandir_desde_centro(s, izquierda, derecha):
        while izquierda >= 0 and derecha < len(s) and s[izquierda] == s[derecha]:
            izquierda -= 1
            derecha += 1
        return s[izquierda + 1: derecha]

    max_palindromo = ""
    for i in range(len(s)):
        palindromo_impar = expandir_desde_centro(s, i, i)
        palindromo_par = expandir_desde_centro(s, i, i + 1)

        max_palindromo = max(max_palindromo, palindromo_impar, palindromo_par, key=len)

    return max_palindromo