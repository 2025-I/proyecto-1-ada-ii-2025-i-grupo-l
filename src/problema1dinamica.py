def subsecuencia_palindromica_dinamica(s: str) -> str:
    """Encuentra la subcadena palindrómica más larga usando programación dinámica."""
    n = len(s)
    if n == 0:
        return ""

    dp = [[False] * n for _ in range(n)]
    inicio, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True

    for longitud in range(2, n + 1):  
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            if s[i] == s[j]:
                if longitud == 2 or dp[i+1][j-1]: 
                    dp[i][j] = True
                    if longitud > max_len:
                        inicio, max_len = i, longitud

    return s[inicio: inicio + max_len]