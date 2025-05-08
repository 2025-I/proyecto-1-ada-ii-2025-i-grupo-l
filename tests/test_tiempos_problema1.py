import os
import matplotlib.pyplot as plt
import numpy as np
import time
import sys

# Agregar el directorio "src" al path para importar las funciones desde otros archivos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from problema1bruta import subsecuencia_palindromica_bruta  # Algoritmo Fuerza Bruta
from problema1dinamica import subsecuencia_palindromica_dinamica  # Algoritmo Dinámico
from problema1voraz import subsecuencia_palindromica_voraz  # Algoritmo Voraz
from problema1 import normalizar_cadena  # Función de normalización de cadena

# Ubicación donde se guardarán las imágenes de los gráficos
output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs', 'imagenes'))
output_path_bruta = os.path.join(output_folder, "grafico_fuerza_bruta.png")
output_path_completo = os.path.join(output_folder, "grafico_comparativo.png")

# Tamaños de prueba para cada algoritmo
tamaños_bruta = [10, 15, 20]  # Pruebas más pequeñas para Fuerza Bruta (evita alto costo computacional)
tamaños_otros = [100, 300, 600, 1000]  # Pruebas más grandes para Dinámica y Voraz

# Función para generar cadenas aleatorias de letras minúsculas
def generar_cadena_aleatoria(longitud):
    return ''.join(np.random.choice(list("abcdefghijklmnopqrstuvwxyz"), longitud))

# Función para medir el tiempo de ejecución de Fuerza Bruta
def medir_tiempo_bruta(entrada):
    inicio = time.time()
    subsecuencia_palindromica_bruta(normalizar_cadena(entrada))
    return time.time() - inicio

# Función para medir el tiempo de ejecución de Dinámica y Voraz
def medir_tiempo_general(algoritmo, entrada):
    inicio = time.time()
    algoritmo(normalizar_cadena(entrada))
    return time.time() - inicio

# Diccionario para almacenar tiempos promedios de ejecución por método
tiempos_promedio = {"Bruta": [], "Dinamica": [], "Voraz": []}

# 🔹 **Evaluar Fuerza Bruta en múltiples tamaños pequeños**
for tamaño in tamaños_bruta:
    print(f"\n📏 Tamaño de prueba Fuerza Bruta: {tamaño}x{tamaño}")
    entradas = [generar_cadena_aleatoria(tamaño) for _ in range(tamaño)]
    
    tiempos_bruta = []

    # Ejecutar 5 repeticiones para obtener un promedio de tiempo
    for i in range(5):
        tiempos_iteracion = [medir_tiempo_bruta(entrada) for entrada in entradas]
        tiempo_promedio_iteracion = sum(tiempos_iteracion) / tamaño  # Promedio por ejecución
        tiempos_bruta.append(tiempo_promedio_iteracion)
        print(f"   🔹 Repetición {i + 1}: {tiempo_promedio_iteracion:.6f} segundos")

    # Calcular el promedio general de Fuerza Bruta
    promedio_bruta = sum(tiempos_bruta) / 5
    tiempos_promedio["Bruta"].append(promedio_bruta)
    print(f"✅ Fuerza Bruta - Tiempo promedio: {promedio_bruta:.6f} segundos")

# 🔹 **Evaluar Dinámica y Voraz con tamaños grandes**
for tamaño in tamaños_otros:
    print(f"\n📏 Tamaño de prueba Dinámica y Voraz: {tamaño}x{tamaño}")
    entradas = [generar_cadena_aleatoria(tamaño) for _ in range(tamaño)]

    tiempos_dinamica, tiempos_voraz = [], []

    # Ejecutar 5 repeticiones para obtener datos precisos
    for i in range(5):
        tiempo_dinamica = sum(medir_tiempo_general(subsecuencia_palindromica_dinamica, entrada) for entrada in entradas)
        tiempos_dinamica.append(tiempo_dinamica)
        print(f"   🔵 Dinámica - Repetición {i + 1}: {tiempo_dinamica:.6f} segundos")

        tiempo_voraz = sum(medir_tiempo_general(subsecuencia_palindromica_voraz, entrada) for entrada in entradas)
        tiempos_voraz.append(tiempo_voraz)
        print(f"   🟢 Voraz - Repetición {i + 1}: {tiempo_voraz:.6f} segundos")

    # Calcular promedios generales
    promedio_dinamica = sum(tiempos_dinamica) / 5
    promedio_voraz = sum(tiempos_voraz) / 5

    tiempos_promedio["Dinamica"].append(promedio_dinamica)
    tiempos_promedio["Voraz"].append(promedio_voraz)

    print(f"✅ Dinámica - Tiempo promedio: {promedio_dinamica:.6f} segundos")
    print(f"✅ Voraz - Tiempo promedio: {promedio_voraz:.6f} segundos")

# 🔥 **Generar gráfico exclusivo para Fuerza Bruta**
plt.figure(figsize=(10, 6))
plt.plot(tamaños_bruta, tiempos_promedio["Bruta"], 'r-o', label="Fuerza Bruta")

# Curva teórica O(n²) para comparación
x_teorico_bruta = np.array(tamaños_bruta)
y_teorico_bruta = x_teorico_bruta**2 / 1e7  
plt.plot(x_teorico_bruta, y_teorico_bruta, 'r--', label="Teórico O(n²) Bruta")

# Configuración del gráfico
plt.xlabel("Tamaño de cadena evaluada")
plt.ylabel("Tiempo de ejecución (s)")
plt.legend()
plt.title("Tiempo de ejecución de Fuerza Bruta")
plt.grid()
plt.savefig(output_path_bruta)
plt.show()
print(f"✅ Gráfico guardado en: {output_path_bruta}")

# 🔥 **Generar gráfico comparativo para Dinámica y Voraz**
plt.figure(figsize=(10, 6))
plt.plot(tamaños_otros, tiempos_promedio["Dinamica"], 'b-o', label="Dinámica")
plt.plot(tamaños_otros, tiempos_promedio["Voraz"], 'g-o', label="Voraz (Manacher)")

# Curvas teóricas
x_teorico = np.array(tamaños_otros)
y_teorico_dinamica = x_teorico**2 / 1e8  
y_teorico_voraz = x_teorico / 1e5  

plt.plot(x_teorico, y_teorico_dinamica, 'b--', label="Teórico O(n²) Dinámica")
plt.plot(x_teorico, y_teorico_voraz, 'g--', label="Teórico O(n) Voraz")

# Configuración del gráfico
plt.xlabel("Tamaño de cadena evaluada")
plt.ylabel("Tiempo de ejecución (s)")
plt.legend()
plt.title("Comparación de tiempos de ejecución - Dinámica vs Voraz")
plt.grid()
plt.savefig(output_path_completo)
plt.show()
print(f"✅ Gráfico guardado en: {output_path_completo}")