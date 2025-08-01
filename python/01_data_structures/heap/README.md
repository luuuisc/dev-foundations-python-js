# 🔺 Heap – Montículos en Python

Esta carpeta contiene implementaciones personalizadas de **heaps** o **montículos**, estructuras especializadas en acceder al valor mínimo o máximo en tiempo constante. Son esenciales en algoritmos como ordenamientos, planificadores y estructuras de prioridad.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `min_heap.py` | Implementación de un montículo mínimo (`min-heap`) |
| `max_heap.py` | Implementación de un montículo máximo (`max-heap`) |

## ▶️ Cómo ejecutar

```bash
python min_heap.py
python max_heap.py
```

Puedes modificar los scripts para ver cómo se comporta la estructura en distintos escenarios.

---

## 🧠 ¿Qué es un heap?

Un **heap** es una estructura de datos basada en árboles binarios **completos**, donde cada nodo cumple una relación específica con sus hijos:

- En un **min-heap**, cada nodo padre es **menor o igual** que sus hijos.
- En un **max-heap**, cada nodo padre es **mayor o igual** que sus hijos.

📌 Aunque se basa en árboles, se implementa típicamente como un **array** (o lista), aprovechando la relación entre índices:

- Hijo izquierdo de `i`: `2i + 1`
- Hijo derecho de `i`: `2i + 2`
- Padre de `i`: `(i - 1) // 2`

---

## ⚙️ Operaciones principales

| Operación | Descripción | Complejidad |
|-----------|-------------|-------------|
| `insert(valor)` | Inserta un nuevo valor manteniendo el orden del heap | `O(log n)` |
| `extract()`     | Elimina y retorna el valor mínimo/máximo | `O(log n)` |
| `peek()`        | Retorna el valor mínimo/máximo sin eliminarlo | `O(1)` |

---

## 📈 Ejemplo de uso

```python
from min_heap import MinHeap

heap = MinHeap()
heap.insert(4)
heap.insert(2)
heap.insert(7)

print(heap.peek())    # 2
print(heap.extract()) # 2
print(heap.extract()) # 4


Y para un MaxHeap:

from max_heap import MaxHeap

heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(15)

print(heap.extract())  # 15
```

## 🌍 Aplicaciones reales de los heaps

| Área | Uso del heap |
|------|--------------|
| 🎮 Videojuegos | Planificación de eventos y tiempos en simulaciones y motores de juego. |
| 🗺️ Navegadores GPS | Algoritmo de Dijkstra para encontrar rutas más cortas usando una cola de prioridad basada en heap. |
| 🖥️ Sistemas operativos | Gestión de prioridades en colas de procesos (CPU scheduling). |
| 🔃 Ordenamiento | Implementación de Heap Sort para ordenar elementos en `O(n log n)`. |
| 🔄 Simulación de eventos | Control del orden temporal en simuladores de tráfico, colas, etc. |
| 📊 Estadísticas y Big Data | Encontrar los `k` elementos más grandes o más pequeños en grandes conjuntos de datos. |
| 💬 Algoritmos de compresión | Usado en Huffman Coding para construir árboles de codificación óptima. |

## 🎯 ¿Por qué implementarlo desde cero?
- Aprender heaps te permite entender estructuras de cola de prioridad
- Mejora tu lógica recursiva y manejo de índices
- Te prepara para entrevistas técnicas y problemas competitivos

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 