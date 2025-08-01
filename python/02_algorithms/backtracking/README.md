# ♟️ Backtracking

El **backtracking** es una técnica de diseño algorítmico que se basa en probar todas las combinaciones posibles y retroceder (backtrack) cuando se detecta que una opción no lleva a una solución válida. Es especialmente útil en problemas de tipo búsqueda, combinación o permutación con restricciones.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `n_queens.py` | Solución al problema clásico de las N reinas utilizando backtracking. |
| `sudoku_solver.py` | Resolver un Sudoku válido mediante exploración de celdas y retroceso. |

---

## ⚙️ ¿Cómo funciona el backtracking?

1. Exploramos una posible solución paso a paso.
2. Si en algún paso la solución parcial no es válida, retrocedemos.
3. Probamos otra opción desde el punto anterior (backtrack).
4. Repetimos hasta encontrar todas las soluciones o una solución válida.

---

## 🧠 ¿Cuándo usarlo?

- Cuando hay muchas combinaciones posibles y se deben **filtrar** por restricciones.
- En **problemas de decisión**, donde se construye la solución paso a paso.
- Casos típicos:
  - Juegos (sudoku, ajedrez)
  - Permutaciones y combinaciones
  - Colorear grafos
  - Solucionar laberintos

---

## 🧪 Cómo ejecutar

```bash
python n_queens.py
python sudoku_solver.py
```

## 🔍 Ejemplo de uso: N Reinas

### `n_queens.py`

```python
from n_queens import solve_n_queens

n = 4
solutions = solve_n_queens(n)

for board in solutions:
    for row in board:
        print(row)
    print("-----")
```

## 🧮 Complejidad esperada

| Algoritmo         | Complejidad Temporal Estimada        | Complejidad Espacial       | Observaciones |
|-------------------|--------------------------------------|-----------------------------|---------------|
| N-Queens          | O(N!)                                | O(N²)                       | Explora todas las posiciones posibles con podas |
| Sudoku Solver     | O(9^(m)) donde m = número de vacíos  | O(1) o O(m) según implementación | El número de llamadas recursivas depende de los espacios vacíos |

## 🌍 Aplicaciones reales

| Aplicación              | Ejemplo                                             |
|-------------------------|-----------------------------------------------------|
| Resolución de juegos    | Sudoku, laberintos, ajedrez                         |
| Problemas combinatorios | Generación de combinaciones/permutaciones          |
| IA y toma de decisiones | Construcción de árboles de decisiones              |
| Validación de restricciones | Verificación de soluciones parciales en tiempo real |

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 
