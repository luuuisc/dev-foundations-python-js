# 🧮 Programación Dinámica (Dynamic Programming)

Esta carpeta contiene ejemplos clásicos de algoritmos que utilizan la técnica de **programación dinámica (DP)** para resolver problemas que pueden descomponerse en subproblemas superpuestos y tener soluciones óptimas estructuradas.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|--------|-------------|
| `fibonacci_dp.py` | Cálculo del n-ésimo número de Fibonacci con memoización |
| `knapsack_dp.py` | Solución al problema de la mochila (0/1 Knapsack) usando DP |
| `longest_common_subsequence.py` | Cálculo de la subsecuencia común más larga entre dos cadenas |

---

## 🧠 ¿Qué es la programación dinámica?

La programación dinámica es un enfoque algorítmico que:

- **Descompone un problema** en subproblemas más pequeños.
- **Guarda los resultados** de subproblemas ya resueltos para evitar cálculos repetidos (*memoización* o *tabulación*).
- Funciona bien en problemas con:
  - **Subproblemas superpuestos**
  - **Estructura óptima**

---

## ⏱️ Complejidad esperada

| Algoritmo                        | Temporal             | Espacial             | Comentarios |
|----------------------------------|----------------------|----------------------|-------------|
| Fibonacci         | O(n)                 | O(n)                 | Se evita la recursión exponencial |
| Knapsack 0/1                     | O(n·W)               | O(n·W)               | `n`: número de ítems, `W`: capacidad |
| Longest Common Subsequence (LCS)| O(n·m)               | O(n·m)               | `n`, `m`: longitudes de las cadenas |

> 💡 *Importante:* Muchas veces podemos **optimizar el espacio** en DP si solo necesitamos una o dos filas previas del arreglo de soluciones.

## 🎯 ¿Por qué es importante?

- Resuelve problemas que serían **exponenciales** con fuerza bruta.
- Es muy común en **entrevistas técnicas**.
- Se aplica en:
  - Optimización de recursos
  - Análisis de secuencias
  - Procesamiento de lenguaje natural

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 
