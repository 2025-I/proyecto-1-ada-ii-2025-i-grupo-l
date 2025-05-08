def subsecuencia_palindromica_dinamica(s: str) -> list:
    """Encuentra todas las subcadenas palindrómicas más largas con programación dinámica."""
    
    n = len(s)  # Obtiene la longitud de la cadena de entrada.
    if n == 0:
        return []  # Retorna una lista vacía si la cadena está vacía.

    # Matriz DP donde dp[i][j] indica si la subcadena s[i:j+1] es un palíndromo.
    dp = [[False] * n for _ in range(n)]
    max_length = 1  # Inicializa la longitud máxima encontrada en 1 (cada letra es un palíndromo).
    palindromos = set()  # Conjunto para almacenar los palíndromos únicos.

    # Caso base: Cada carácter es un palíndromo por sí solo.
    for i in range(n):
        dp[i][i] = True
        palindromos.add(s[i])  # Agregamos cada letra como un palíndromo mínimo.

    # Evaluamos todas las subcadenas de longitud creciente.
    for longitud in range(2, n + 1):  
        for i in range(n - longitud + 1):
            j = i + longitud - 1  # Determina el índice final de la subcadena actual.

            # Verificamos si la subcadena es un palíndromo usando la matriz DP.
            if s[i] == s[j] and (longitud == 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if longitud > max_length:
                    max_length = longitud  # Actualizamos el tamaño máximo encontrado.
                    palindromos = {s[i:j + 1]}  # Reiniciamos con la nueva mejor solución.
                elif longitud == max_length:
                    palindromos.add(s[i:j + 1])  # Agregamos soluciones óptimas.

    # Ordenamos los resultados según su posición original en la cadena.
    return sorted(list(palindromos), key=lambda x: s.index(x))