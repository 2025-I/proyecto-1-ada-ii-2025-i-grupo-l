import tkinter as tk
from tkinter import filedialog
from problema2 import resolver_fiesta

def abrir_archivo_y_resolver_fiesta():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    if not file_path:
        print("No se seleccionó archivo.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lineas = f.read().splitlines()

    num_casos = int(lineas[0])
    indice = 1  # línea actual

    print("\nRESULTADOS DEL PROBLEMA DE LA FIESTA\n")

    for caso in range(num_casos):
        n = int(lineas[indice])
        matriz = []
        for i in range(indice + 1, indice + 1 + n):
            fila = list(map(int, lineas[i].split()))
            matriz.append(fila)
        convivencias = list(map(int, lineas[indice + 1 + n].split()))

        resultados = resolver_fiesta(matriz, convivencias)
        print(f"\nCaso {caso + 1}: (n = {n})")
        for estrategia, (invitados, convivenciasT) in resultados.items():
            print(f"  {estrategia.capitalize()} -> Invitados: {invitados}, Total: {convivenciasT}")

        # Mover al siguiente bloque
        indice = indice + 1 + n + 1

# Ejecutar solo si se llama directamente
if __name__ == "__main__":
    abrir_archivo_y_resolver_fiesta()
