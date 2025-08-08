"""
adjacency_matrix.py
Representación de grafos usando **matriz de adyacencia**.

Características:
- Soporta grafos dirigidos o no dirigidos.
- Soporta pesos (por defecto 1.0) o no ponderados (bool).
- Operaciones: añadir vértices/aristas, eliminar, vecinos, etc.

Complejidad típica:
- add_edge/get_edge: O(1)
- neighbors(v): O(V)
- Espacio: O(V^2)

Uso:
    g = GraphMatrix(directed=False, weighted=False)
    a = g.add_vertex("A")
    b = g.add_vertex("B")
    g.add_edge(a, b)
    print(g.neighbors(a))  # [(1, 1.0)]
"""

from typing import Any, List, Tuple, Optional


class GraphMatrix:
    def __init__(self, directed: bool = False, weighted: bool = True, default_weight: float = 1.0):
        self.directed = directed
        self.weighted = weighted
        self.default_weight = default_weight
        self.vertices: List[Any] = []
        self.matrix: List[List[float]] = []  # 0.0 = sin arista; >0 = peso

    # ---- Vértices ----
    def add_vertex(self, label: Any) -> int:
        """Agrega un vértice y devuelve su índice."""
        self.vertices.append(label)
        n = len(self.vertices)
        # expandir filas existentes
        for row in self.matrix:
            row.append(0.0)
        # nueva fila
        self.matrix.append([0.0] * n)
        return n - 1

    def index_of(self, label: Any) -> Optional[int]:
        try:
            return self.vertices.index(label)
        except ValueError:
            return None

    # ---- Aristas ----
    def add_edge(self, u: int, v: int, weight: Optional[float] = None) -> None:
        """Añade arista u->v (y v->u si no dirigido)."""
        w = self._resolve_weight(weight)
        self._check_vertex(u)
        self._check_vertex(v)
        self.matrix[u][v] = w
        if not self.directed:
            self.matrix[v][u] = w

    def remove_edge(self, u: int, v: int) -> None:
        """Elimina arista u->v (y v->u si no dirigido)."""
        self._check_vertex(u)
        self._check_vertex(v)
        self.matrix[u][v] = 0.0
        if not self.directed:
            self.matrix[v][u] = 0.0

    def has_edge(self, u: int, v: int) -> bool:
        self._check_vertex(u)
        self._check_vertex(v)
        return self.matrix[u][v] != 0.0

    def get_weight(self, u: int, v: int) -> Optional[float]:
        """Devuelve peso si existe arista; de lo contrario None."""
        self._check_vertex(u)
        self._check_vertex(v)
        return self.matrix[u][v] or None

    # ---- Consultas ----
    def neighbors(self, u: int) -> List[Tuple[int, float]]:
        """Lista de (vecino, peso) para u."""
        self._check_vertex(u)
        res = []
        row = self.matrix[u]
        for v, w in enumerate(row):
            if w != 0.0:
                res.append((v, w))
        return res

    def order(self) -> int:
        return len(self.vertices)

    def size(self) -> int:
        e = sum(1 for i in range(self.order()) for j in range(self.order()) if self.matrix[i][j] != 0.0)
        return e if self.directed else e // 2

    # ---- Helpers ----
    def _check_vertex(self, i: int) -> None:
        if not (0 <= i < len(self.vertices)):
            raise IndexError("Índice de vértice inválido")

    def _resolve_weight(self, w: Optional[float]) -> float:
        if not self.weighted:
            return 1.0
        return float(self.default_weight if w is None else w)

    # ---- Representación ----
    def __repr__(self) -> str:
        return f"GraphMatrix(V={self.order()}, E={self.size()}, directed={self.directed}, weighted={self.weighted})"


if __name__ == "__main__":
    g = GraphMatrix(directed=False, weighted=True)
    ia = g.add_vertex("A")
    ib = g.add_vertex("B")
    ic = g.add_vertex("C")

    g.add_edge(ia, ib, 2.5)
    g.add_edge(ib, ic, 1.0)

    print(g)
    print("Vecinos de B:", g.neighbors(ib))
    print("Peso(B,C):", g.get_weight(ib, ic))
