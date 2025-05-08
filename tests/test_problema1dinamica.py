import unittest
import sys
import os
import time
import random
import string

# Agregar el directorio "src" al path para importar los módulos del problema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from problema1dinamica import subsecuencia_palindromica_dinamica
from problema1 import normalizar_cadena

# Función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    return cadena == cadena[::-1]  # Retorna True si la cadena es igual a su reverso

# Función para generar cadenas aleatorias con letras y números
def generar_cadena_aleatoria(longitud):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=longitud))  # Crea una cadena aleatoria

class TestDinamica(unittest.TestCase):
    """Pruebas unitarias para el algoritmo de Programación Dinámica de subsecuencia palindrómica más larga."""

    def test_palindromos_dinamica(self):
        """Ejecuta pruebas con diferentes tamaños de entrada y valida que el resultado sea un palíndromo."""

        # Diccionario con diferentes tamaños de prueba
        tamaños = {
            "Juguete": [  # Pruebas con frases predefinidas, donde el resultado esperado es un palíndromo específico
                ("Dábale arroz a la zorra el abad", ["dabalearrozalazorraelabad"]),
                ("Se es o no se es un ministro", ["seesonosees"]),
                ("Yo dono rosas, oro no doy", ["yodonorosasoronodoy"]),
                ("reconocer", ["reconocer"]),
                ("anilina", ["anilina"]),
                ("oso", ["oso"]),
                ("radar", ["radar"]),
                ("¿Acaso hubo búhos acá?", ["acasohubobuhosaca"]),
                ("La ruta natural.", ["larutanatural"]),
                ("A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá", ["amamaromaleavivaelamorapapayapaparomaleavivaelamoramama"])
            ],
            "Pequeño": [generar_cadena_aleatoria(100) for _ in range(100)],  # Cadenas aleatorias de 100 caracteres
            "Mediano": [generar_cadena_aleatoria(1000) for _ in range(1000)],  # Cadenas aleatorias de 1000 caracteres
            "Grande": [generar_cadena_aleatoria(2000) for _ in range(2000)],  # Cadenas aleatorias de 2000 caracteres
            "Extra grande": [generar_cadena_aleatoria(3000) for _ in range(3000)],  # Cadenas de gran tamaño
        }

        # Iterar sobre cada conjunto de pruebas (Juguete, Pequeño, Mediano, Grande)
        for nombre, entradas in tamaños.items():
            print(f"\nTest {nombre} - Evaluando {len(entradas)} cadenas")

            tiempos_totales = []  # Lista para almacenar tiempos totales por prueba

            for _ in range(5):  # Ejecutar cada prueba 5 veces para obtener valores promedio
                tiempos = []  # Lista de tiempos individuales por ejecución

                for entrada in entradas:
                    # Normalizar la cadena de entrada (remueve caracteres no relevantes)
                    normalizada = normalizar_cadena(entrada if isinstance(entrada, str) else entrada[0])

                    # Medir el tiempo de ejecución del algoritmo de Programación Dinámica
                    inicio = time.time()
                    resultado = subsecuencia_palindromica_dinamica(normalizada)
                    tiempo = time.time() - inicio
                    tiempos.append(tiempo)  # Almacenar el tiempo de ejecución

                    # Validación específica en los casos de "Juguete"
                    if nombre == "Juguete":
                        palabra_esperada = entrada[1][0]  # Obtener el resultado esperado
                        self.assertEqual(resultado[0], palabra_esperada, f"❌ Error en Juguete - entrada: {entrada[0]}")
                        print(f"\n   ➜ Palabra evaluada: \"{entrada[0]}\"")
                        print(f"   🔹 Palabra esperada: \"{palabra_esperada}\"")
                        print(f"   🔵 Dinámica: \"{resultado[0]}\" ({tiempo:.6f} segundos) ✅ Correcto")

                    # Validación en pruebas con tamaños grandes (la salida debe ser un palíndromo)
                    elif nombre != "Juguete":
                        self.assertTrue(es_palindromo(resultado[0]), f"❌ No es palíndromo en {nombre}: {resultado[0]}")

                # Guardar el tiempo total por ejecución
                tiempos_totales.append(sum(tiempos))

            # Calcular y mostrar el tiempo promedio en pruebas grandes
            if nombre != "Juguete":
                print(f"   🔵 Dinámica - Tiempo promedio en {nombre}: {sum(tiempos_totales) / 5:.6f} segundos")

if __name__ == "__main__":
    unittest.main()