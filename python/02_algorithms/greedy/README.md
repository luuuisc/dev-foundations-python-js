# 💰 Algoritmos Greedy (Voraces)

Los **algoritmos greedy** son una técnica de diseño algorítmico que construye soluciones paso a paso **tomando en cada paso la opción que parece más prometedora** en ese momento, con la esperanza de que esta elección local lleve a una solución global óptima.

Se caracterizan por:
- **Tomar decisiones locales óptimas** en cada paso.
- No reconsiderar elecciones previas.
- Funcionar bien solo si el problema cumple **propiedad de subestructura óptima** y **propiedad de elección voraz**.

---

## 📂 Archivos incluidos

| Archivo                | Descripción |
|------------------------|-------------|
| `activity_selection.py` | Selección de actividades con el mayor número de tareas compatibles en un intervalo de tiempo. |
| `coin_change.py`        | Resolución del problema de cambio de monedas minimizando la cantidad de monedas utilizadas (en casos donde el enfoque voraz es óptimo). |

---

## 🧠 ¿Cuándo usar un algoritmo greedy?

Un algoritmo greedy funciona correctamente cuando:
1. **Propiedad de subestructura óptima**: una solución óptima del problema contiene soluciones óptimas para subproblemas.
2. **Propiedad de elección voraz**: siempre se puede construir una solución óptima eligiendo la mejor opción disponible en cada paso.

Ejemplos de problemas adecuados:
- Selección de actividades
- Árbol generador mínimo (Prim, Kruskal)
- Codificación de Huffman
- Planificación de recursos con prioridad

---

## ⏱️ Complejidad esperada

| Algoritmo             | Temporal          | Espacial | Notas |
|-----------------------|-------------------|----------|-------|
| Selección de actividades | O(n log n) (por el ordenamiento) | O(1) | Se ordena por hora de finalización |
| Coin Change (greedy)  | O(n)              | O(1)     | Solo óptimo en sistemas de monedas específicos |

---

## 🧪 Ejemplo rápido: Coin Change

```python
from coin_change import coin_change

coins = [25, 10, 5, 1]
amount = 63
print(coin_change(coins, amount))
# [25, 25, 10, 1, 1, 1]
```

---

## 🌍 Aplicaciones reales

| Área                | Ejemplo                                                        |
| ------------------- | -------------------------------------------------------------- |
| Finanzas            | Devolución de cambio con la menor cantidad de monedas/billetes |
| Planificación       | Asignación de recursos y tiempos                               |
| Redes               | Protocolos de transmisión eficiente                            |
| Compresión de datos | Codificación de Huffman                                        |

---

## 📚 Top 5 recursos recomendados

1. **[Greedy Algorithms - GeeksforGeeks](https://www.geeksforgeeks.org/greedy-algorithms/)** – Ejemplos y teoría detallada.
2. **[Greedy Algorithms - Princeton](https://algs4.cs.princeton.edu/43mst/)** – Aplicaciones clásicas como MST y Huffman.
3. **Libro: "Introduction to Algorithms" (CLRS)** – Capítulo dedicado a greedy con demostraciones de optimalidad.
5. **[LeetCode Greedy Problems](https://leetcode.com/tag/greedy/)** – Colección de ejercicios prácticos.

---

## 🙌 Créditos

Desarrollado con fines educativos ❤️ por [@luuiscc\_](https://github.com/luuuisc)

