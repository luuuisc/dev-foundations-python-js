# 🔍 Algoritmos de Búsqueda

Los **algoritmos de búsqueda** permiten localizar un elemento dentro de una colección de datos.  
Dependiendo de si la colección está **ordenada** o **desordenada**, se utilizan diferentes estrategias con distintos niveles de eficiencia.

---

## 📂 Archivos incluidos

| Archivo             | Descripción |
|---------------------|-------------|
| `linear_search.py`  | Búsqueda secuencial en listas no ordenadas |
| `binary_search.py`  | Búsqueda binaria en listas ordenadas |
| `jump_search.py`    | Búsqueda por saltos en listas ordenadas |

---

## 🧠 Teoría general

### 1. Búsqueda lineal (Linear Search)
- Recorre la lista elemento por elemento hasta encontrar el objetivo o llegar al final.
- Funciona en listas **ordenadas** o **no ordenadas**.
- **Complejidad:**  
  - Tiempo: O(n)  
  - Espacio: O(1)

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

---

### 2. Búsqueda binaria (Binary Search)

* Requiere que la lista esté **ordenada**.
* Compara el elemento central con el objetivo y descarta la mitad donde no puede estar.
* **Complejidad:**

  * Tiempo: O(log n)
  * Espacio: O(1) (iterativa) o O(log n) (recursiva)

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

---

### 3. Búsqueda por saltos (Jump Search)

* Requiere lista **ordenada**.
* Salta bloques de tamaño fijo (aproximadamente `√n`) hasta superar el objetivo, luego realiza búsqueda lineal en ese bloque.
* **Complejidad:**

  * Tiempo: O(√n)
  * Espacio: O(1)

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    return prev if arr[prev] == target else -1
```

---

## 📊 Comparativa de complejidad

| Algoritmo     | Orden de la lista | Tiempo promedio | Tiempo peor caso | Espacio                   |
| ------------- | ----------------- | --------------- | ---------------- | ------------------------- |
| Linear Search | No necesario      | O(n)            | O(n)             | O(1)                      |
| Binary Search | Ordenada          | O(log n)        | O(log n)         | O(1) / O(log n) recursiva |
| Jump Search   | Ordenada          | O(√n)           | O(√n)            | O(1)                      |

---

## 📊 Ejemplo visual: Búsqueda binaria

Lista ordenada:

```
[2, 5, 8, 12, 16, 23, 38, 45, 72, 91]
```

Buscar `23`:

1. Mitad: índice 4 → valor 16 → buscar en la derecha.
2. Mitad: índice 7 → valor 45 → buscar en la izquierda.
3. Mitad: índice 5 → valor 23 → encontrado.

---

## 🌍 Aplicaciones reales

| Algoritmo     | Aplicaciones                                                                 |
| ------------- | ---------------------------------------------------------------------------- |
| Linear Search | Listas cortas, búsqueda en datos no ordenados                                |
| Binary Search | Diccionarios, bases de datos, búsqueda en ficheros indexados                 |
| Jump Search   | Búsquedas rápidas en memoria o discos cuando el acceso secuencial es costoso |

---

## 📚 Top recursos recomendados

1. **[Searching Algorithms - GeeksforGeeks](https://www.geeksforgeeks.org/searching-algorithms/)** – Explicaciones y ejemplos detallados.
2. **[Binary Search - Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)** – Animaciones interactivas.
3. **Libro: "Introduction to Algorithms" (CLRS)** – Capítulos sobre búsqueda y ordenamiento.

---

## 🙌 Créditos

Desarrollado con fines educativos ❤️ por [@luuiscc\_](https://github.com/luuuisc)
