"""
traversal.py
Recorridos y utilidades generales de grafos que funcionan con:
- GraphMatrix (matriz de adyacencia)
- GraphList (lista de adyacencia)

Incluye:
- BFS (Breadth-First Search)
- DFS (iterativo y recursivo)
- Camino más corto no ponderado (via BFS)
- Topological sort (Kahn) para DAGs dirigidos

Requisitos: el objeto grafo debe exponer:
- order() -> int
- neighbors(u) -> List[Tuple[int, weight]]
"""

from collections import deque
from typing import List, Tuple, Optional


def bfs(graph, source: int) -> List[int]:
    """Devuelve el orden de visita desde `source` usando BFS."""
    n = graph.order()
    visited = [False] * n
    order = []
    q = deque([source])
    visited[source] = True

    while q:
        u = q.popleft()
        order.append(u)
        for v, _ in graph.neighbors(u):
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return order


def dfs_iterative(graph, source: int) -> List[int]:
    """DFS iterativo."""
    n = graph.order()
    visited = [False] * n
    order = []
    stack = [source]

    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            order.append(u)
            # apilar vecinos en orden inverso para comportamiento similar al recursivo
            for v, _ in reversed(graph.neighbors(u)):
                if not visited[v]:
                    stack.append(v)
    return order


def dfs_recursive(graph, source: int) -> List[int]:
    """DFS recursivo."""
    n = graph.order()
    visited = [False] * n
    order = []

    def _dfs(u: int):
        visited[u] = True
        order.append(u)
        for v, _ in graph.neighbors(u):
            if not visited[v]:
                _dfs(v)

    _dfs(source)
    return order


def unweighted_shortest_path(graph, source: int, target: int) -> Optional[List[int]]:
    """
    Camino más corto en grafos no ponderados (o donde el peso no importa).
    Devuelve la lista de índices de vértices desde source hasta target, o None si no hay camino.
    """
    n = graph.order()
    prev = [-1] * n
    q = deque([source])
    prev[source] = source

    while q:
        u = q.popleft()
        if u == target:
            break
        for v, _ in graph.neighbors(u):
            if prev[v] == -1:
                prev[v] = u
                q.append(v)

    if prev[target] == -1:
        return None

    # reconstrucción
    path = []
    cur = target
    while cur != source:
        path.append(cur)
        cur = prev[cur]
    path.append(source)
    path.reverse()
    return path


def topological_sort_kahn(graph) -> List[int]:
    """
    Orden topológico (Kahn). Requiere grafo dirigido sin ciclos (DAG).
    Si detecta ciclo, devuelve lista vacía.
    """
    n = graph.order()
    indeg = [0] * n
    for u in range(n):
        for v, _ in graph.neighbors(u):
            indeg[v] += 1

    q = deque([i for i in range(n) if indeg[i] == 0])
    result = []

    while q:
        u = q.popleft()
        result.append(u)
        for v, _ in graph.neighbors(u):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return result if len(result) == n else []


if __name__ == "__main__":
    # Pequeña demo usando lista de adyacencia
    from adjacency_list import GraphList

    g = GraphList(directed=True, weighted=False)
    a = g.add_vertex("A")
    b = g.add_vertex("B")
    c = g.add_vertex("C")
    d = g.add_vertex("D")

    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(c, d)

    print("BFS desde A:", bfs(g, a))
    print("DFS iterativo desde A:", dfs_iterative(g, a))
    print("DFS recursivo desde A:", dfs_recursive(g, a))
    print("Camino más corto A->D:", unweighted_shortest_path(g, a, d))
    print("Topological sort:", topological_sort_kahn(g))
