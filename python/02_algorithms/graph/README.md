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

Un **grafo** es una estructura que representa relaciones entre objetos mediante **nodos (vértices)** y **conexiones (aristas)**. Puede ser:

- **Dirigido** o **no dirigido**
- **Ponderado** o **no ponderado**
- **Cíclico** o **acíclico**

---

## ⏱️ Complejidad esperada

| Algoritmo           | Complejidad temporal | Complejidad espacial | Notas |
|---------------------|----------------------|----------------------|-------|
| Dijkstra (con heap) | O((V + E) log V)     | O(V)                 | Grafos con pesos positivos |
| Kruskal             | O(E log E)           | O(V)                 | Usa estructura de conjuntos disjuntos |
| Prim (con heap)     | O((V + E) log V)     | O(V)                 | Alternativa a Kruskal |
| Topological Sort    | O(V + E)             | O(V)                 | Solo válido en DAGs |

---

## ✨ Aplicaciones comunes

| Algoritmo         | Aplicaciones |
|-------------------|--------------|
| Dijkstra          | Navegación GPS, redes de computadoras, videojuegos |
| Kruskal & Prim    | Infraestructura, redes eléctricas, optimización de costos |
| Topological Sort  | Compilación de dependencias, planificadores de tareas |

---

## 🧭 ¿Por qué aprender estos algoritmos?

- Son esenciales en ciencias de la computación y optimización.
- Forman parte del núcleo de muchas bibliotecas y motores de búsqueda.
- Aparecen frecuentemente en entrevistas técnicas y competencias de programación.

---

> Siguiente paso: profundizar en estructuras auxiliares como heaps y conjuntos disjuntos (`Union-Find`) para optimizar estos algoritmos.

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 

