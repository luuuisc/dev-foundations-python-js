# ♟️ Backtracking

El **backtracking** es una técnica de diseño algorítmico basada en la **búsqueda exhaustiva con retroceso**. Consiste en explorar todas las posibles soluciones a un problema, construyendo la respuesta paso a paso. Si en algún momento se detecta que la solución parcial no puede llevar a un resultado válido, se **retrocede** (“backtrack”) al paso anterior y se prueba una alternativa distinta.  

Es una estrategia común en problemas de **búsqueda en espacios de soluciones** donde existen restricciones que permiten descartar rápidamente ramas enteras del árbol de posibilidades.

---

## 📂 Archivos incluidos

| Archivo              | Descripción |
|----------------------|-------------|
| `n_queens.py`        | Implementación del problema clásico de las N reinas utilizando backtracking. |
| `sudoku_solver.py`   | Resolución de un Sudoku válido mediante exploración de celdas y retroceso. |

---

## ⚙️ ¿Cómo funciona el backtracking?

1. **Exploración progresiva**: Se construye la solución paso a paso.
2. **Verificación parcial**: En cada paso se valida si la solución parcial cumple las restricciones.
3. **Retroceso**: Si la solución parcial no es válida, se regresa al estado anterior y se prueba otra opción.
4. **Búsqueda completa o temprana**: El proceso continúa hasta encontrar **todas** las soluciones posibles o detenerse tras hallar la **primera solución válida**.

Este proceso se puede visualizar como un **árbol de decisiones**, donde cada nodo representa un estado parcial de la solución y las ramas representan las elecciones posibles.

---

## 🧠 ¿Cuándo usarlo?

- Cuando el número de soluciones posibles es alto, pero se pueden **descartar rápidamente** muchas de ellas con restricciones.
- En problemas que requieren **enumerar combinaciones, permutaciones o disposiciones**.
- En contextos donde se construye la solución paso a paso y se puede interrumpir al detectar un error.

**Casos típicos:**
- Juegos y rompecabezas (Sudoku, ajedrez, laberintos)
- Problemas combinatorios
- Coloreo de grafos
- Búsqueda de rutas con restricciones

---

## 🧪 Ejemplo rápido: N Reinas

```python
from n_queens import solve_n_queens

n = 4
solutions = solve_n_queens(n)

for board in solutions:
    for row in board:
        print(row)
    print("-----")
````

Salida esperada:

```
.Q..
...Q
Q...
..Q.
-----
..Q.
Q...
...Q
.Q..
-----
```

---

## 🧮 Complejidad esperada

| Algoritmo     | Complejidad Temporal Aproximada | Complejidad Espacial | Observaciones                              |
| ------------- | ------------------------------- | -------------------- | ------------------------------------------ |
| N-Queens      | O(N!)                           | O(N²)                | El uso de podas reduce el tiempo real      |
| Sudoku Solver | O(9^m) donde m = celdas vacías  | O(m) o O(1)          | Altamente dependiente del número de vacíos |

---

## 🌍 Aplicaciones reales

| Área                        | Ejemplo                                                |
| --------------------------- | ------------------------------------------------------ |
| Resolución de juegos        | Sudoku, ajedrez, laberintos                            |
| Problemas combinatorios     | Generar todas las combinaciones válidas de un conjunto |
| IA y toma de decisiones     | Construcción de árboles de juego                       |
| Validación de restricciones | Verificación de reglas en tiempo real                  |

---

## 📚 Top 5 recursos recomendados

1. **[Backtracking - GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)** – Explicación teórica con ejemplos clásicos.
2. **[Backtracking Pattern - LeetCode Explore](https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/)** – Ejercicios progresivos para dominar el patrón.

---

## 🙌 Créditos

Desarrollado con fines educativos ❤️ por [@luuiscc\_](https://github.com/luuuisc)
