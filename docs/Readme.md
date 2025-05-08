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

-
### Problema de la fiesta


---

### 📈 Análisis de tiempos de ejecución para matriz de 25x25

![calculo_tiempo_matriz_grande](./imagenes/calculo_tiempo_matriz_grande.png)


Se midió el tiempo de ejecución de las tres estrategias implementadas (fuerza bruta, programación dinámica y voraz) utilizando una matriz jerárquica de tamaño **25 x 25**.

Los resultados fueron los siguientes:

![grafica_tiempos](./imagenes/tiempos_25.png)


```
Fuerza Bruta:           66.31 segundos
Programación Dinámica:   0.00085 segundos
Voraz:                   0.00016 segundos
```

#### 🧠 Interpretación

* La **estrategia de fuerza bruta**, aunque garantiza encontrar la solución óptima, presenta un **tiempo de ejecución extremadamente alto**, incluso con una entrada moderada de 25 elementos. Esto se debe a su complejidad exponencial, ya que evalúa todas las combinaciones posibles de empleados respetando las restricciones del problema.

* La **programación dinámica** logra encontrar la solución óptima de forma **casi instantánea** gracias a la utilización de subestructuras óptimas propias de árboles, reduciendo drásticamente el espacio de búsqueda.

* La **estrategia voraz** es la más rápida de todas, ya que realiza una selección lineal de nodos basada en el valor de convivencia sin explorar el espacio completo. Sin embargo, esta estrategia no siempre garantiza un resultado óptimo.

#### 📌 Conclusión del experimento fiesta

Este experimento demuestra cómo el enfoque adecuado (en este caso, la programación dinámica) puede ofrecer una **solución óptima y eficiente** incluso para estructuras jerárquicas medianas, mientras que el enfoque voraz puede ser útil en escenarios donde la eficiencia es prioritaria sobre la exactitud. Por otro lado, el enfoque de fuerza bruta **no escala adecuadamente** y solo es práctico para casos de prueba pequeños.

---




## 🛠️ Automatización con GitHub Actions

Se configuró un pipeline en `.github/workflows/python-app.yml` para ejecutar automáticamente:

- Instalación de dependencias
- Ejecución de pruebas unitarias con `pytest`
- Validación de integridad del proyecto

Esto asegura que todos los cambios sean probados antes de integrarse a la rama principal.

---

## ✅ Conclusiones

- La estrategia de **programación dinámica** es ideal para encontrar soluciones óptimas en problemas estructurados como árboles.
- El enfoque **voraz**, aunque eficiente, puede llevar a resultados incorrectos o subóptimos si se valida contra una solución exacta.
- Automatizar pruebas con GitHub Actions mejora la confiabilidad del desarrollo.

---

