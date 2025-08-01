# 🕸️ Graph – Estructuras de grafos en Python

Esta carpeta contiene implementaciones básicas de **estructuras de grafos** y algunos algoritmos fundamentales de recorrido. Los grafos son estructuras no lineales compuestas por nodos (vértices) y conexiones entre ellos (aristas), ampliamente utilizados en redes, mapas, inteligencia artificial, compiladores, etc.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|--------|-------------|
| `adjacency_list.py` | Implementación de un grafo utilizando lista de adyacencia |
| `adjacency_matrix.py` | Implementación de un grafo utilizando matriz de adyacencia |
| `traversal.py` | Algoritmos de recorrido: BFS (Breadth-First Search) y DFS (Depth-First Search) |

## ▶️ Cómo usar

Ejecuta cada script directamente para ver ejemplos de uso:

```bash
python adjacency_list.py
python adjacency_matrix.py
python traversal.py
```

---

## 🧠 ¿Qué es un grafo?

Un **grafo** está formado por:
- Un conjunto de **vértices** (o nodos)
- Un conjunto de **aristas** (o conexiones) que unen pares de vértices

Puede ser:
- **Dirigido** (las conexiones tienen dirección) o **no dirigido**
- **Ponderado** (las aristas tienen peso) o **no ponderado**

---

## 🧮 Representaciones comunes de grafos

### ✅ Lista de adyacencia (`adjacency_list.py`)
Eficiente en espacio para grafos dispersos.

```python
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
```

Ventajas:
- Menor uso de memoria
- Fácil de recorrer


### ✅ Matriz de adyacencia (`adjacency_matrix.py`)

Ideal para grafos densos o cuando se requiere verificar rápidamente si existe una conexión entre dos nodos.

```text
    A  B  C
A [ 0, 1, 1 ]
B [ 1, 0, 0 ]
C [ 1, 0, 0 ]
```

Ventajas:
- Verificación rápida de conexiones
- Buena para algoritmos que requieren operaciones matriciales

### 🔁 Algoritmos de recorrido (`traversal.py`)

🔹 BFS – Breadth-First Search
- Usa una cola (queue)
- Recorre el grafo nivel por nivel

🔹 DFS – Depth-First Search
- Usa una pila (implícitamente con recursión o explícitamente)
- Se sumerge en un camino antes de retroceder

Estos algoritmos sirven para:
- Encontrar caminos
- Detectar ciclos
- Clasificar dependencias
- Resolver rompecabezas y más

## 🌍 ¿Para qué sirven los grafos?

Los grafos son una herramienta esencial para representar y resolver problemas en los que hay elementos conectados entre sí. Desde redes sociales hasta navegación GPS, modelan relaciones, rutas, dependencias y estructuras en sistemas complejos.

Un grafo permite representar:
- Personas y sus relaciones
- Lugares y las rutas entre ellos
- Computadoras y sus conexiones
- Tareas y sus dependencias
- Páginas web y sus enlaces
- Elementos químicos y sus reacciones

## 🏙️ Aplicaciones de grafos en la vida cotidiana y profesional

| Área | Ejemplo de uso | Explicación |
|------|----------------|-------------|
| 🔗 Redes sociales | Facebook, Twitter, Instagram | Cada usuario es un nodo; las amistades, seguidores o menciones son aristas. Los algoritmos de sugerencia de amigos usan caminos y vecinos comunes. |
| 🛰️ Navegación y mapas | Google Maps, Waze | Las ciudades y calles son nodos; las rutas, aristas con peso (distancia o tráfico). Los algoritmos buscan el camino más corto o rápido. |
| 🌐 Web e internet | Google, motores de búsqueda | Cada página web es un nodo; los enlaces entre páginas son aristas. El algoritmo PageRank de Google se basa en grafos. |
| 🛒 Recomendaciones | Amazon, Netflix, Spotify | Los productos, usuarios o canciones se conectan en un grafo para detectar patrones, similitudes o gustos en común. |
| 💻 Redes de computadoras | Diseño de redes LAN/WAN | Los dispositivos (routers, switches, PCs) son nodos; los cables o conexiones inalámbricas, las aristas. Se usa para optimizar rutas y detectar fallas. |
| 🔄 Dependencias en software | NPM, Python, compiladores | Los módulos se conectan en un grafo dirigido que muestra qué depende de qué. Es vital para compilación, actualización o carga de paquetes. |
| 🧬 Biología y medicina | Genómica, redes neuronales | Las neuronas, genes o proteínas están conectadas y su interacción puede modelarse con grafos para estudiar el comportamiento de sistemas complejos. |
| 📊 Bases de datos | Bases de datos orientadas a grafos como Neo4j | Permiten consultar relaciones complejas de forma más eficiente que bases de datos relacionales tradicionales. Muy útiles en análisis de fraudes o genealogía. |
| 🤖 Inteligencia Artificial | Planificación, razonamiento | En IA, los grafos se usan para representar estados, transiciones y relaciones semánticas entre conceptos (grafos de conocimiento). |

## 🎯 ¿Por qué es importante aprender grafos?
- Porque muchos problemas del mundo real son relacionales: tráfico, relaciones humanas, circuitos, procesos, redes…
- Porque dominar sus algoritmos (BFS, DFS, Dijkstra, A*, Kruskal, etc.) es esencial para entrevistas técnicas y resolución de problemas complejos.
- Porque entrenar modelos, construir apps inteligentes o diseñar sistemas eficientes depende muchas veces de saber estructurar y recorrer un grafo.

## 🔎 Ejemplo cotidiano:
Cuando abres Waze y te recomienda evitar una avenida por tráfico, está usando un grafo donde cada calle es un nodo conectado a otras calles, y cada conexión tiene un peso que representa el tiempo estimado. Luego, usa un algoritmo como Dijkstra para hallar la ruta más rápida.

## 📚 Recomendaciones
- Empieza con adjacency_list.py para entender la estructura más intuitiva
- Usa `traversal.py` para practicar recorridos y entender cómo se explora un grafo
- Modifica los grafos de prueba para ver cómo cambian los recorridos


## 🙌 Créditos

Esta carpeta fue desarrollada como parte del proyecto de estructuras de datos en Python.

Autor: [@luuiscc_](https://github.com/luuuisc) 

> Entender grafos es entender cómo se conecta el mundo.