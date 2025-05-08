# 📊 Informe del Proyecto 1 - Análisis de Algoritmos II (2025-I)

**Nombre del estudiante:** Kevin Andres Bejarano y Juan David Gutierrez  
**Curso:** ADA II - Ingeniería de Sistemas  
**Periodo:** 2025-I  
**Profesor(a):** [Carlos Andres Delgado Saavedra]

---

## 🧩 Descripción General del Proyecto

Este proyecto busca resolver dos problemas representativos en el análisis y comparación de algoritmos: uno relacionado con cadenas (subsecuencias palindrómicas) y otro con estructuras jerárquicas (organización de una fiesta sin conflictos entre jefes y subordinados). Cada problema fue resuelto utilizando tres estrategias clásicas:

- Fuerza bruta
- Programación dinámica
- Algoritmo voraz (greedy)

El objetivo es comparar precisión, eficiencia y escalabilidad entre estas estrategias.

---

## 🔹 Problema 1: Subsecuencia Palindrómica Más Larga

### 🧠 Enunciado

Dada una cadena de caracteres, se debe encontrar la subsecuencia más larga que sea un palíndromo. Se deben ignorar signos de puntuación, espacios y mayúsculas/minúsculas.

### ✅ Entrada esperada

- Número de cadenas a analizar.
- Una cadena por línea.

### 🔁 Salida esperada

- Una línea por cadena, que contiene la subsecuencia palindrómica más larga.

### 🛠️ Estrategias implementadas

- **Fuerza bruta:** genera todas las subsecuencias posibles.
- **Programación dinámica:** aplica la técnica de subproblemas óptimos usando una matriz `n x n`.
- **Voraz:** explora pares extremos y toma decisiones locales (menos preciso, pero rápido).

---

## 🔹 Problema 2: Planeación de la Fiesta de la Compañía

### 🧠 Enunciado

En una organización representada como un árbol jerárquico, se debe seleccionar el subconjunto de empleados con mayor puntuación de convivencia, **sin incluir jefes y subordinados directos en el mismo grupo**.

### ✅ Entrada esperada

- Número de matrices a evaluar.
- Para cada caso:
  - Número de empleados `n`.
  - Matriz `n x n` donde `matriz[i][j] = 1` indica que `i` es jefe directo de `j`.
  - Lista de puntuaciones de convivencia para cada empleado.

### 🔁 Salida esperada

- Por cada caso:
  - Vector binario que indica qué empleados van a la fiesta.
  - Puntaje total de convivencia de los seleccionados.

### 🛠️ Estrategias implementadas

- **Fuerza bruta:** evalúa todas las combinaciones válidas. Solo viable para n pequeños.
- **Programación dinámica:** solución óptima basada en postorden del árbol.
- **Voraz:** elige empleados con mayor puntaje primero, excluyendo sus jefes e hijos.

---

## 🧪 Resultados y Pruebas

### 🔬 Tipos de pruebas realizadas

- **Casos manuales** (verificación visual).
- **Casos automáticos pequeños:** Por razones de capacidad solo se implementaron pruebas con pesos maximos de 25 x 25 en cuanto a las matrices.
- **Casos de rendimiento:** 1.000, 10.000, hasta 50.000 empleados (excepto en fuerza bruta).


