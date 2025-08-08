# 🌐 Algoritmos de Grafos

Esta carpeta incluye implementaciones fundamentales de algoritmos sobre **estructuras de grafos**, utilizados para resolver problemas como caminos más cortos, árboles generadores mínimos y ordenamientos topológicos.

---

## 📂 Archivos incluidos

| Archivo                  | Descripción |
|--------------------------|-------------|
| `dijkstra.py`            | Algoritmo de Dijkstra para caminos más cortos desde un origen |
| `kruskal.py`             | Algoritmo de Kruskal para obtener el árbol generador mínimo |
| `prim.py`                | Algoritmo de Prim para árbol generador mínimo |
| `topological_sort.py`    | Ordenamiento topológico en grafos dirigidos acíclicos (DAGs) |

---

## 🧠 ¿Qué son los grafos?

Un **grafo** es una estructura de datos que representa relaciones entre objetos mediante **nodos (vértices)** y **conexiones (aristas)**.  

Los grafos pueden clasificarse en:

- **Dirigidos** y **no dirigidos**  
- **Ponderados** y **no ponderados**  
- **Cíclicos** y **acíclicos**  

Matemáticamente, un grafo se define como `G = (V, E)` donde:
- `V` es el conjunto de vértices.
- `E` es el conjunto de aristas (pares de vértices).

---

## ⚙️ Descripción breve de los algoritmos

1. **Dijkstra** – Encuentra la ruta más corta desde un nodo origen a todos los demás en un grafo con pesos positivos.  
2. **Kruskal** – Encuentra el Árbol Generador Mínimo (MST) uniendo aristas de menor peso sin formar ciclos.  
3. **Prim** – Construye el MST expandiendo desde un nodo inicial, eligiendo siempre la arista más barata hacia un nuevo vértice.  
4. **Topological Sort** – Ordena los vértices de un grafo dirigido acíclico en un orden lineal tal que para cada arista (u, v), u aparece antes que v.

---

## ⏱️ Complejidad esperada

| Algoritmo           | Complejidad temporal | Complejidad espacial | Notas |
|---------------------|----------------------|----------------------|-------|
| Dijkstra (con heap) | O((V + E) log V)     | O(V)                 | Solo con pesos positivos |
| Kruskal             | O(E log E)           | O(V)                 | Usa Union-Find para optimizar |
| Prim (con heap)     | O((V + E) log V)     | O(V)                 | Más eficiente con estructuras de prioridad |
| Topological Sort    | O(V + E)             | O(V)                 | Solo válido en DAGs |

---

## 🧪 Ejemplo rápido: Dijkstra

```python
from dijkstra import dijkstra

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 1, 'C': 3, 'D': 6}
```

---

## ✨ Aplicaciones comunes

| Algoritmo        | Aplicaciones                                                         |
| ---------------- | -------------------------------------------------------------------- |
| Dijkstra         | Navegación GPS, redes de computadoras, IA en videojuegos             |
| Kruskal & Prim   | Diseño de redes eléctricas, cableado, rutas de transporte            |
| Topological Sort | Compiladores, planificación de proyectos, resolución de dependencias |

---

## 📚 Top 5 recursos recomendados

1. **[Graph Algorithms - GeeksforGeeks](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)** – Explicaciones detalladas y ejemplos en código.
2. **[Princeton Algorithms: Graphs](https://algs4.cs.princeton.edu/41graph/)** – Recurso académico con teoría sólida.
3. **[Introduction to Graph Theory - MIT OpenCourseWare](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2005/pages/lecture-notes/)** – Curso completo gratuito.
4. **Libro: "Introduction to Algorithms" (CLRS)** – Capítulos 22-24 sobre grafos y algoritmos clásicos.
5. **[NetworkX Documentation](https://networkx.org/documentation/stable/)** – Librería de Python para trabajar con grafos.

---

## 🙌 Créditos

Desarrollado con fines educativos ❤️ por [@luuiscc\_](https://github.com/luuuisc)
