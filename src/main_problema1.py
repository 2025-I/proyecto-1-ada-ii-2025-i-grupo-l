import tkinter as tk
from tkinter import filedialog
from problema1 import normalizar_cadena, encontrar_palindromos  # Se usa la función principal

def seleccionar_archivo():
    """Abre un cuadro de diálogo para que el usuario seleccione un archivo de texto."""
    root = tk.Tk()  # Inicializa una ventana oculta de tkinter
    root.withdraw()  # Oculta la ventana principal para que solo aparezca el diálogo
    archivo_path = filedialog.askopenfilename(
        title="Selecciona un archivo de texto",
        filetypes=[("Archivos de texto", "*.txt")]  # Filtra para archivos de texto solamente
    )
    return archivo_path  # Retorna la ruta del archivo seleccionado

def ejecutar_algoritmos(archivo_path):
    """Lee el archivo y encuentra la subsecuencia palindrómica más larga en cada línea."""
    
    # Validar que se haya seleccionado un archivo
    if not archivo_path:
        print("⚠ No se seleccionó ningún archivo.")
        return

    # Abrir el archivo en modo lectura y obtener las líneas
    with open(archivo_path, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()  # Leer todas las líneas del archivo
        n = int(lineas[0].strip())  # Primera línea del archivo indica el número de cadenas a analizar

        # Validar que el número de líneas coincida con la cantidad esperada
        if len(lineas) - 1 < n:
            print("⚠ Error: El número de cadenas no coincide con las líneas disponibles.")
            return

        # Iterar sobre cada línea para analizar los palíndromos
        for i in range(1, n + 1):  
            linea_normalizada = normalizar_cadena(lineas[i].strip())  # Limpia la cadena de espacios y caracteres especiales

            # Ejecuta los tres algoritmos para encontrar la subsecuencia palindrómica más larga
            resultados = encontrar_palindromos(linea_normalizada)

            # Imprimir los resultados en consola
            print(f"🔹 Fuerza Bruta: {resultados['bruta']}")  # Resultado del algoritmo de Fuerza Bruta
            print(f"🔹 Programación Dinámica: {resultados['dinámica']}")  # Resultado del algoritmo Dinámico
            print(f"🔹 Expansión desde el Centro (Voraz): {resultados['voraz']}")  # Resultado del algoritmo Voraz

# Ejecutar la selección y análisis de archivo al correr el script
if __name__ == "__main__":
    archivo = seleccionar_archivo()  # Abre el diálogo de selección de archivo
    ejecutar_algoritmos(archivo)  # Procesa el archivo seleccionado