def subsecuencia_palindromica_voraz(s_original: str) -> list:
    """Encuentra todas las subcadenas palindrómicas más largas usando Manacher."""

    # Convertimos la cadena insertando caracteres separadores '#' para manejar casos de palíndromos pares.
    s = '#' + '#'.join(s_original) + '#'
    n = len(s)
    p = [0] * n  # Array que almacena el radio de expansión de cada centro de palíndromo.
    c, r = 0, 0  # Variables para el centro y el radio del palíndromo más grande encontrado hasta el momento.

    # Aplicamos el algoritmo de Manacher
    for i in range(n):
        mirror = 2 * c - i  # Calculamos la posición espejo en referencia a `c`.

        # Si `i` está dentro del radio `r`, inicializamos `p[i]` basado en su reflejo.
        if i < r:
            p[i] = min(r - i, p[mirror])

        # Expandimos alrededor del centro `i`, verificando que los caracteres sean iguales.
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and s[i - p[i] - 1] == s[i + p[i] + 1]:
            p[i] += 1

        # Actualizamos el nuevo centro `c` y su límite derecho `r` si la expansión superó `r`.
        if i + p[i] > r:
            c, r = i, i + p[i]

    # Determinamos el tamaño máximo encontrado en la expansión de palíndromos.
    max_length = max(p)
    palindromos = {s[i - max_length: i + max_length].replace("#", "") for i in range(n) if p[i] == max_length}

    # Ordenamos los resultados según su posición en la cadena original.
    return sorted(list(palindromos), key=lambda x: s_original.find(x))