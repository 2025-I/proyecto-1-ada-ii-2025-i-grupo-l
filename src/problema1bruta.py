def subsecuencia_palindromica_bruta(s: str) -> list:
    """Encuentra todas las subcadenas palindrómicas más largas sin duplicados."""
    
    n = len(s)  # Calcula la longitud de la cadena de entrada.
    max_length = 0  # Variable para almacenar la longitud del palíndromo más largo encontrado.
    palindromos = set()  # Conjunto para almacenar los palíndromos únicos encontrados.

    # Recorremos todas las posibles subcadenas
    for i in range(n):
        for j in range(i, n):
            subcadena = s[i:j + 1]  # Extraemos la subcadena desde `i` hasta `j`.

            # Verificamos si la subcadena es un palíndromo (comparándola con su versión invertida).
            if subcadena == subcadena[::-1]:
                if len(subcadena) > max_length:
                    max_length = len(subcadena)  # Actualizamos el tamaño máximo encontrado.
                    palindromos = {subcadena}  # Reiniciamos el conjunto con la nueva mejor solución.
                elif len(subcadena) == max_length:
                    palindromos.add(subcadena)  # Agregamos soluciones óptimas del mismo tamaño.

    return sorted(list(palindromos))  # Convertimos el conjunto en una lista ordenada antes de retornarlo.