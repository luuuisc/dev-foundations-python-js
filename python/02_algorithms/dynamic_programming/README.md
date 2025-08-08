# 🧮 Programación Dinámica (Dynamic Programming)

La **programación dinámica (DP)** es una técnica de diseño de algoritmos que permite resolver problemas complejos dividiéndolos en **subproblemas más pequeños** cuyos resultados se almacenan para evitar cálculos repetidos.  

Es especialmente útil cuando un problema presenta:
- **Subproblemas superpuestos**: los mismos subproblemas se resuelven múltiples veces.
- **Estructura óptima**: la solución óptima del problema completo se puede construir a partir de soluciones óptimas de sus subproblemas.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|--------|-------------|
| `fibonacci_dp.py` | Cálculo del n-ésimo número de Fibonacci con memoización |
| `knapsack_dp.py` | Solución al problema de la mochila (0/1 Knapsack) usando DP |
| `longest_common_subsequence.py` | Cálculo de la subsecuencia común más larga entre dos cadenas |

---

## ⚙️ ¿Cómo funciona la programación dinámica?

Existen dos enfoques principales:

1. **Memoización (Top-Down)**  
   - Se usa recursión.
   - Se almacenan los resultados de las llamadas ya resueltas en una tabla (generalmente un diccionario o arreglo).
   - Evita recomputar subproblemas.

2. **Tabulación (Bottom-Up)**  
   - Se construye una tabla de soluciones empezando por los casos base.
   - Se resuelve el problema de forma iterativa.
   - Suele ser más eficiente en consumo de memoria en ciertos casos.

---

## 🧪 Ejemplo rápido: Fibonacci con memoización

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))  # 55
```
---

## ⏱️ Complejidad esperada

| Algoritmo                        | Temporal | Espacial | Comentarios                          |
| -------------------------------- | -------- | -------- | ------------------------------------ |
| Fibonacci                        | O(n)     | O(n)     | Se evita la recursión exponencial    |
| Knapsack 0/1                     | O(n·W)   | O(n·W)   | `n`: número de ítems, `W`: capacidad |
| Longest Common Subsequence (LCS) | O(n·m)   | O(n·m)   | `n`, `m`: longitudes de las cadenas  |

---

## 🌍 Aplicaciones reales

| Área                      | Ejemplo                                       |
| ------------------------- | --------------------------------------------- |
| Optimización de recursos  | Planificación de proyectos, rutas óptimas     |
| Bioinformática            | Alineación de secuencias de ADN               |
| Procesamiento de lenguaje | Corrección ortográfica, traducción automática |
| Finanzas                  | Estrategias de inversión óptimas              |
| Compresión de datos       | Algoritmos como Lempel–Ziv                    |

---

## 📚 Top 5 recursos recomendados

1. **[Dynamic Programming - GeeksforGeeks](https://www.geeksforgeeks.org/dynamic-programming/)** – Ejemplos y teoría detallada.
2. **[DP Patterns - LeetCode Explore](https://leetcode.com/explore/learn/card/dynamic-programming/)** – Ejercicios guiados para dominar el patrón.
3. **Libro: "Introduction to Algorithms" (CLRS)** – Capítulos dedicados a DP con análisis de complejidad y ejemplos.

---

## 🙌 Créditos

Desarrollado con fines educativos ❤️ por [@luuiscc\_](https://github.com/luuuisc)

