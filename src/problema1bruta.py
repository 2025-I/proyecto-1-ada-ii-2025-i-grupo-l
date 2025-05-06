def subsecuencia_palindromica_bruta(s: str) -> str:
    """Encuentra la subcadena palindrómica más larga usando fuerza bruta."""
    n = len(s)
    max_palindromo = ""

    for i in range(n):
        for j in range(i, n):
            subcadena = s[i:j + 1]
            if subcadena == subcadena[::-1] and len(subcadena) > len(max_palindromo):
                max_palindromo = subcadena

    return max_palindromo