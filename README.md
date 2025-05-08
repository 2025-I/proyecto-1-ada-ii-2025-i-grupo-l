[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kKWtV-CB)
# Ejemplo de titulo de Taller
PROGRAMACION DINAMICA Y VORAZ
## Integrantes

KEVIN ANDRES BEJARANO TELLO | 2067678
JUAN DAVID GUTIERREZ FLOREZ | 2060104


## Descripción


Este proyecto resuelve dos problemas clásicos de análisis de algoritmos utilizando tres enfoques distintos: **fuerza bruta**, **programación dinámica** y **algoritmos voraces**, haciendo énfasis en la optimización y análisis de complejidad computacional.

---

## 🧠 Problema 1: Subsecuencias palindrómicas más largas

Se debe encontrar la subsecuencia palindrómica más larga de una cadena de entrada, ignorando mayúsculas, minúsculas y caracteres no alfanuméricos.

**Entrada:**  
- Número de cadenas a procesar.  
- Cada línea contiene una cadena.

**Salida esperada:**  
- Una línea por cadena, con el palíndromo más largo en minúsculas.

Se implementaron las tres estrategias para comparar rendimiento y calidad de solución.

---

## 🎉 Problema 2: Planeando una fiesta de la compañía

El objetivo es invitar a los empleados de una empresa (representados en un árbol jerárquico) maximizando su nivel de convivencia, con la restricción de que **ningún jefe y su subordinado directo pueden asistir juntos**.

**Entrada:**  
- Número de matrices a procesar.  
- Para cada problema:
  - Número de empleados.
  - Matriz de supervisión (adyacencia dirigida).
  - Lista de puntuaciones de convivencia por empleado.

**Salida esperada:**  
- Para cada matriz, un vector binario (empleado invitado: 1 o 0) y la suma total de convivencia.

Se implementan y comparan tres enfoques:
- Fuerza bruta: evalúa todas las combinaciones posibles válidas.
- Programación dinámica: solución óptima con subestructuras óptimas en árboles.
- Algoritmo voraz: elige nodos con mayor convivencia, respetando restricciones.

---




