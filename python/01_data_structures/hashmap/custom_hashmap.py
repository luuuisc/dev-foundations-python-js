"""
custom_hashmap.py
Implementación simple de un HashMap (tabla hash) con **encadenamiento** y **redimensionamiento**.

Características:
- Buckets como listas (chaining).
- Redimensiona automáticamente cuando se supera el factor de carga (load factor).
- Operaciones: put, get, remove, contains, len, items, keys, values.

Complejidad esperada:
- Promedio: O(1) para put/get/remove.
- Peor caso: O(n) si todas las claves colisionan en un mismo bucket.
"""

from typing import Any, Iterable, Iterator, List, Tuple, Optional


class HashMap:
    def __init__(self, initial_capacity: int = 8, load_factor: float = 0.75):
        if initial_capacity < 1:
            raise ValueError("initial_capacity debe ser >= 1")
        self._capacity = 1
        # capacidad como potencia de 2 (ayuda a distribuir con hash % capacity)
        while self._capacity < initial_capacity:
            self._capacity <<= 1

        self._buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(self._capacity)]
        self._size = 0
        self._load_factor = load_factor

    # ------------- utilidades internas -------------
    def _bucket_index(self, key: Any) -> int:
        return hash(key) & (self._capacity - 1)  # equivalente a % cuando capacidad es potencia de 2

    def _should_resize(self) -> bool:
        return (self._size / self._capacity) > self._load_factor

    def _resize(self, new_capacity: int) -> None:
        old_buckets = self._buckets
        self._capacity = new_capacity
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)

    # ------------- API pública -------------
    def put(self, key: Any, value: Any) -> None:
        """Inserta o actualiza (key -> value)."""
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1

        if self._should_resize():
            self._resize(self._capacity * 2)

    def get(self, key: Any, default: Any = None) -> Any:
        """Devuelve el valor asociado o `default` si no existe. Lanza KeyError si default es None y no existe."""
        idx = self._bucket_index(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        if default is not None:
            return default
        raise KeyError(f"Clave no encontrada: {key!r}")

    def remove(self, key: Any) -> None:
        """Elimina la clave si existe; si no existe lanza KeyError."""
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(f"Clave no encontrada: {key!r}")

    def contains(self, key: Any) -> bool:
        """True si la clave existe."""
        idx = self._bucket_index(key)
        return any(k == key for k, _ in self._buckets[idx])

    # ------------- utilidades de iteración -------------
    def items(self) -> Iterator[Tuple[Any, Any]]:
        for bucket in self._buckets:
            for kv in bucket:
                yield kv

    def keys(self) -> Iterator[Any]:
        for k, _ in self.items():
            yield k

    def values(self) -> Iterator[Any]:
        for _, v in self.items():
            yield v

    # ------------- protocolos útiles -------------
    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"HashMap(size={self._size}, capacity={self._capacity}, load_factor={self._load_factor})"


if __name__ == "__main__":
    # Demo rápida
    m = HashMap(initial_capacity=4, load_factor=0.75)
    m.put("nombre", "Luis")
    m.put("edad", 30)
    m.put("pais", "MX")
    m.put("stack", "Python")

    print(m)
    print("nombre:", m.get("nombre"))
    print("edad existe?", m.contains("edad"))
    print("items:", list(m.items()))

    m.remove("edad")
    print("edad existe?", m.contains("edad"))
    print(m)
