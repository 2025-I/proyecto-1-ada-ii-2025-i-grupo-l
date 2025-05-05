import tkinter as tk
from tkinter import filedialog
from problema1 import normalizar_cadena, encontrar_palindromos  # Se usa la función principal

def seleccionar_archivo():
    """Abre un diálogo para seleccionar el archivo de entrada."""
    root = tk.Tk()
    root.withdraw()
    archivo_path = filedialog.askopenfilename(title="Selecciona un archivo de texto", filetypes=[("Archivos de texto", "*.txt")])
    return archivo_path

def ejecutar_algoritmos(archivo_path):
    """Lee el archivo y encuentra la subcadena palindrómica más larga en cada línea."""
    if not archivo_path:
        print("⚠ No se seleccionó ningún archivo.")
        return

    with open(archivo_path, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        n = int(lineas[0].strip())  

        if len(lineas) - 1 < n:
            print("⚠ Error: El número de cadenas no coincide con las líneas disponibles.")
            return

        for i in range(1, n + 1):  
            linea_normalizada = normalizar_cadena(lineas[i].strip())

            resultados = encontrar_palindromos(linea_normalizada)

            print(f"🔹 Fuerza Bruta: {resultados['bruta']}")
            print(f"🔹 Programación Dinámica: {resultados['dinámica']}")
            print(f"🔹 Expansión desde el Centro (Voraz): {resultados['voraz']}")

if __name__ == "__main__":
    archivo = seleccionar_archivo()
    ejecutar_algoritmos(archivo)