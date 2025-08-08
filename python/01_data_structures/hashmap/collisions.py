"""
collisions.py
Demostraciones de **colisiones** y dos estrategias de resolución:
- Encadenamiento (usa HashMap del archivo custom_hashmap.py).
- Direccionamiento abierto (linear probing) con una implementación mínima para fines didácticos.
"""

from __future__ import annotations
from typing import Any, Iterator, List, Tuple, Optional

from custom_hashmap import HashMap


# --------- Utilidad para forzar colisiones ---------
class BadKey:
    """
    Clave con hash constante para forzar colisiones.
    Dos BadKey diferentes NO son iguales (se comparan por identidad).
    """
    def __init__(self, label: str) -> None:
        self.label = label

    def __hash__(self) -> int:
        return 42  # mismo hash para todos

    def __eq__(self, other: object) -> bool:
        return self is other  # distintas instancias nunca serán iguales

    def __repr__(self) -> str:
        return f"BadKey({self.label})"


# --------- Direccionamiento abierto: Linear Probing (mínimo educativo) ---------
_EMPTY = object()
_DELETED = object()


class LinearProbingHashMap:
    """
    Implementación educativa de HashMap con **linear probing**.
    - No estable / no segura para concurrencia; solo para fines didácticos.
    - Redimensiona al superar el load factor.
    """
    def __init__(self, initial_capacity: int = 8, load_factor: float = 0.6) -> None:
        cap = 1
        while cap < initial_capacity:
            cap <<= 1
        self._capacity = cap
        self._load_factor = load_factor
        self._size = 0
        self._keys: List[Any] = [_EMPTY] * self._capacity
        self._values: List[Any] = [_EMPTY] * self._capacity

    def _probe(self, key: Any) -> int:
        idx = hash(key) & (self._capacity - 1)
        first_deleted = -1
        while True:
            k = self._keys[idx]
            if k is _EMPTY:
                return first_deleted if first_deleted != -1 else idx
            if k is _DELETED:
                if first_deleted == -1:
                    first_deleted = idx
            elif k == key:
                return idx
            idx = (idx + 1) & (self._capacity - 1)

    def _should_resize(self) -> bool:
        return (self._size / self._capacity) > self._load_factor

    def _resize(self, new_capacity: int) -> None:
        old_k = self._keys
        old_v = self._values
        self._capacity = new_capacity
        self._keys = [_EMPTY] * new_capacity
        self._values = [_EMPTY] * new_capacity
        self._size = 0
        for k, v in zip(old_k, old_v):
            if k is not _EMPTY and k is not _DELETED:
                self.put(k, v)

    def put(self, key: Any, value: Any) -> None:
        idx = self._probe(key)
        if self._keys[idx] == key:
            self._values[idx] = value
        else:
            self._keys[idx] = key
            self._values[idx] = value
            self._size += 1
            if self._should_resize():
                self._resize(self._capacity * 2)

    def get(self, key: Any, default: Any = None) -> Any:
        idx = hash(key) & (self._capacity - 1)
        while True:
            k = self._keys[idx]
            if k is _EMPTY:
                if default is not None:
                    return default
                raise KeyError(key)
            if k is not _DELETED and k == key:
                return self._values[idx]
            idx = (idx + 1) & (self._capacity - 1)

    def remove(self, key: Any) -> None:
        idx = hash(key) & (self._capacity - 1)
        while True:
            k = self._keys[idx]
            if k is _EMPTY:
                raise KeyError(key)
            if k is not _DELETED and k == key:
                self._keys[idx] = _DELETED
                self._values[idx] = _DELETED
                self._size -= 1
                return
            idx = (idx + 1) & (self._capacity - 1)

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"LinearProbingHashMap(size={self._size}, capacity={self._capacity})"


# --------- Demos ---------
def demo_chaining():
    print("\n=== Encadenamiento (HashMap con buckets-lista) ===")
    hm = HashMap(initial_capacity=4, load_factor=0.9)

    keys = [BadKey(f"k{i}") for i in range(6)]
    for i, k in enumerate(keys):
        hm.put(k, f"val{i}")

    # Todos caen en el mismo bucket (colisión intencional)
    bucket_idx = None
    if keys:
        # acceder al bucket utilizando el método interno (solo para la demo)
        bucket_idx = hash(keys[0]) & (hm._capacity - 1)  # type: ignore[attr-defined]
        bucket = hm._buckets[bucket_idx]                 # type: ignore[attr-defined]
        print("Bucket usado para todas las claves:", bucket_idx)
        print("Contenido del bucket:", bucket)

    # Lecturas
    print("Lecturas correctas:")
    for i, k in enumerate(keys):
        print(f"  {k!r} ->", hm.get(k))


def demo_linear_probing():
    print("\n=== Direccionamiento abierto (Linear Probing) ===")
    lp = LinearProbingHashMap(initial_capacity=8, load_factor=0.7)

    # Usamos BadKey para forzar mismo hash; linear probing los separa en celdas contiguas
    keys = [BadKey(f"k{i}") for i in range(6)]
    for i, k in enumerate(keys):
        lp.put(k, f"val{i}")

    print(lp)
    # Mostrar posiciones utilizadas
    used = [(i, lp._keys[i], lp._values[i]) for i in range(lp._capacity) if lp._keys[i] is not _EMPTY]  # demo
    print("Slots ocupados (idx, key, value):")
    for t in used:
        print(" ", t)

    # Lecturas
    print("Lecturas correctas:")
    for i, k in enumerate(keys):
        print(f"  {k!r} ->", lp.get(k))


if __name__ == "__main__":
    demo_chaining()
    demo_linear_probing()
