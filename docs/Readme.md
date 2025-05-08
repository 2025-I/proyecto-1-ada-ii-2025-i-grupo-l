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
    ![funcion_bruta](./imagenes/funcion_bruta.png)

        

    ---

    ### 🔹 `obtener_relaciones(matriz)`

    * Construye una lista de relaciones jefe → subordinado a partir de la matriz de adyacencia.
    * Cada índice `i` contiene una lista con los nodos `j` donde `matriz[i][j] == 1`.

    ---

    ### 🔹 `es_valido(invitados, relaciones)`

    * Verifica si un conjunto de invitados es válido.
    * Recorre cada invitado y revisa que **ningún subordinado directo suyo** también esté invitado.
    * Si hay algún conflicto, retorna `False`; si no, `True`.

    ---

    ### 🔹 `fiestaFuerzaBruta(matriz, convivencias)`

    1. Extrae el número de empleados.

    2. Obtiene las relaciones jerárquicas.

    3. Inicializa variables para guardar la mejor combinación de invitados y el puntaje más alto.

    4. Genera todas las combinaciones posibles de invitados para todos los tamaños (1 a n).

    5. Para cada combinación:

    * Verifica si es válida.
    * Calcula la suma de convivencias.
    * Si supera la mejor, actualiza los valores.

    6. Devuelve:

    * Un vector binario (`1` = invitado, `0` = no invitado).
    * El mejor puntaje total encontrado.

    ---




- **Programación dinámica:** solución óptima basada en postorden del árbol.
  ![funcion_dp](./imagenes/funcion_dp.png)



    ---

    ### 🔹 `construir_arbol(matriz)`

    * Recorre la matriz de adyacencia y construye un diccionario `hijos` con las relaciones padre → hijos.
    * Marca quiénes son hijos (`es_hijo[]`) para encontrar la **raíz del árbol**.
    * Retorna la jerarquía y el nodo raíz.

    ---

    ### 🔹 `dp_fiesta(nodo, hijos, convivencias, dp)`

    * Función recursiva con **memoización** (guarda resultados ya calculados en `dp`).

    * Para cada nodo, calcula dos escenarios:

    1. **Incluir el nodo** actual:

        * Se suma su valor de convivencia.
        * Se agregan los valores de **excluir** a sus hijos (para evitar conflictos).
    2. **Excluir el nodo**:

        * Se calcula el mejor resultado posible (mayor valor) entre **incluir o excluir** cada hijo.

    * Devuelve tres cosas:

    * Lista binaria si se incluye.
    * Lista binaria si se excluye.
    * Puntaje total del mejor caso.

    ---

    ### 🔹 `fiesta_programacion_dinamica(matriz, convivencias)`

    1. Construye el árbol y obtiene la raíz.
    2. Llama a `dp_fiesta` desde la raíz para obtener todas las decisiones óptimas.
    3. Compara:

    * El puntaje total si se incluye la raíz.
    * El puntaje total si se excluye.
    4. Retorna:

    * El mejor conjunto de invitados (como lista binaria).
    * La mejor puntuación de convivencia total.

    ---




- **Voraz:** elige empleados con mayor puntaje primero, excluyendo sus jefes e hijos.
    ![funcion_voraz](./imagenes/funcion_voraz.png)

  

    ---

    ### 🔹 `fiesta_voraz(matriz, convivencias)`

    #### 1. **Inicialización**

    * `n`: número de empleados.
    * `seleccion`: lista binaria de empleados invitados (inicialmente todos `0`).
    * `no_disponibles`: conjunto de empleados que no pueden ser invitados porque ya están relacionados (como jefe o subordinado).

    #### 2. **Construcción de relaciones**

    * Se crean los diccionarios `hijos` y `padres` para cada nodo con base en la matriz de adyacencia.
    * `matriz[i][j] == 1` indica que el empleado `i` es jefe directo de `j`.

    #### 3. **Ordenamiento por prioridad**

    * Los nodos se ordenan de mayor a menor convivencia.
    * Esto permite intentar invitar primero a los empleados con mayor valor.

    #### 4. **Selección voraz**

    * Se recorre la lista ordenada.
    * Si el nodo actual no está marcado como no disponible:

    * Se marca como invitado.
    * Se marcan como no disponibles sus jefes y subordinados directos (para evitar conflicto jerárquico).

    #### 5. **Cálculo del total**

    * Se suman las convivencias de los nodos seleccionados.

    #### 6. **Retorno**

    * Devuelve:

    * La lista binaria de invitados.
    * El puntaje total acumulado.

    ---



---



     

---



## 🧪 Resultados y Pruebas

### 🔬 Tipos de pruebas realizadas

-
### Problema de la fiesta


---

### 📈 Análisis de tiempos de ejecución para matriz de 25x25

![calculo_tiempo_matriz_grande](./imagenes/calculo_tiempos_matriz_grande.png)


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

