"""
adjacency_list.py
Representación de grafos usando **lista de adyacencia**.

Características:
- Dirigido o no dirigido.
- Ponderado o no ponderado.
- Ideal para grafos dispersos (sparse).

Complejidad típica:
- add_edge: O(1)
- neighbors(v): O(grado(v))
- Espacio: O(V + E)

Uso:
    g = GraphList(directed=True, weighted=False)
    g.add_vertex("A"); g.add_vertex("B")
    g.add_edge(0, 1)
    print(g.neighbors(0))  # [(1, 1.0)]
"""

from typing import Any, List, Tuple, Dict, Optional


class GraphList:
    def __init__(self, directed: bool = False, weighted: bool = True, default_weight: float = 1.0):
        self.directed = directed
        self.weighted = weighted
        self.default_weight = default_weight
        self.vertices: List[Any] = []
        self.adj: Dict[int, List[Tuple[int, float]]] = {}

    # ---- Vértices ----
    def add_vertex(self, label: Any) -> int:
        idx = len(self.vertices)
        self.vertices.append(label)
        self.adj[idx] = []
        return idx

    def index_of(self, label: Any) -> Optional[int]:
        try:
            return self.vertices.index(label)
        except ValueError:
            return None

    # ---- Aristas ----
    def add_edge(self, u: int, v: int, weight: Optional[float] = None) -> None:
        self._check_vertex(u)
        self._check_vertex(v)
        w = self._resolve_weight(weight)
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

    def remove_edge(self, u: int, v: int) -> None:
        self._check_vertex(u)
        self._check_vertex(v)
        self.adj[u] = [(x, w) for (x, w) in self.adj[u] if x != v]
        if not self.directed:
            self.adj[v] = [(x, w) for (x, w) in self.adj[v] if x != u]

    def neighbors(self, u: int) -> List[Tuple[int, float]]:
        self._check_vertex(u)
        return list(self.adj[u])

    # ---- Métricas ----
    def order(self) -> int:
        return len(self.vertices)

    def size(self) -> int:
        e = sum(len(lst) for lst in self.adj.values())
        return e if self.directed else e // 2

    # ---- Helpers ----
    def _check_vertex(self, i: int) -> None:
        if i not in self.adj:
            raise IndexError("Índice de vértice inválido")

    def _resolve_weight(self, w: Optional[float]) -> float:
        if not self.weighted:
            return 1.0
        return float(self.default_weight if w is None else w)

    def __repr__(self) -> str:
        return f"GraphList(V={self.order()}, E={self.size()}, directed={self.directed}, weighted={self.weighted})"


if __name__ == "__main__":
    g = GraphList(directed=True, weighted=False)
    a = g.add_vertex("A")
    b = g.add_vertex("B")
    c = g.add_vertex("C")
    g.add_edge(a, b)
    g.add_edge(b, c)
    print(g)
    print("Vecinos de B:", g.neighbors(b))
