# 🔃 Algoritmos de Ordenamiento (Sorting)

Los **algoritmos de ordenamiento** reorganizan elementos (números, cadenas, objetos) siguiendo un criterio (p. ej., ascendente).  
Son fundamentales para acelerar búsquedas, deduplicación, combinaciones y análisis de datos.

---

## 📂 Archivos incluidos

| Archivo              | Descripción |
|----------------------|-------------|
| `bubble_sort.py`     | Ordenamiento burbuja (intercambios adyacentes) |
| `insertion_sort.py`  | Inserción directa (construye una lista ordenada) |
| `selection_sort.py`  | Selección del mínimo en cada pasada |
| `merge_sort.py`      | Divide y vencerás; mezcla listas ordenadas |
| `quick_sort.py`      | Divide y vencerás; partición alrededor de un pivote |
| `heap_sort.py`       | Usa un heap binario para extraer máximos/mínimos |

---

## 🧠 Teoría esencial

Los algoritmos de ordenamiento son una de las bases de la informática, ya que muchos otros algoritmos (de búsqueda, optimización, estructuras de datos) dependen de tener los datos ordenados para funcionar de manera eficiente.

Algunos conceptos clave:

- **Estabilidad**: Un algoritmo es estable si, cuando dos elementos tienen la misma clave, mantienen el mismo orden relativo que tenían antes de ordenar.  
  Ejemplo: si ordenas una lista de personas por edad y dos personas tienen la misma edad, un algoritmo estable mantendrá su orden original.

- **In-place**: El algoritmo no necesita una estructura auxiliar proporcional al tamaño de la lista; usa solo una cantidad constante de memoria extra (O(1)). Esto es importante cuando se trabaja con grandes volúmenes de datos.

- **Comparativo vs No comparativo**:
  - **Comparativos**: Deciden el orden solo mediante comparaciones (`<`, `>`). Ejemplos: Quick Sort, Merge Sort, Heap Sort.
  - **No comparativos**: Usan operaciones distintas a la comparación para ordenar, como el conteo o distribución de elementos (p. ej., *Counting Sort*, *Radix Sort*). Pueden ser más rápidos en casos específicos pero dependen de propiedades concretas de los datos.

- **Complejidad temporal**:  
  - *Mejor caso*: escenario más favorable (ej. lista ya ordenada para Insertion Sort).  
  - *Promedio*: escenario más común esperado.  
  - *Peor caso*: escenario menos favorable (ej. Quick Sort con pivote desbalanceado).

- **Complejidad espacial**: Espacio extra requerido además de los datos originales.

- **Divide y vencerás**: Estrategia en la que el problema se divide en subproblemas más pequeños, se resuelven de forma independiente y luego se combinan. Merge Sort y Quick Sort usan esta técnica.

- **Trade-offs**: No hay un único algoritmo “mejor” para todo; la elección depende de:
  - Tamaño de los datos.
  - Distribución de los elementos.
  - Restricciones de memoria.
  - Necesidad o no de estabilidad.

---

## ⚙️ Descripción rápida de cada algoritmo

- **Bubble Sort**: burbujea el mayor hacia el final con intercambios adyacentes. Simple, educativo, **ineficiente**.
- **Insertion Sort**: inserta cada elemento en su posición dentro de la parte ya ordenada. Excelente para **listas pequeñas** o **casi ordenadas**.
- **Selection Sort**: selecciona el mínimo y lo pone al inicio. Pocos movimientos, pero comparaciones cuadráticas.
- **Merge Sort**: divide la lista y **mezcla** dos mitades ordenadas. Complejidad `O(n log n)` garantizada, **estable**, pero no in-place.
- **Quick Sort**: elige **pivote**, particiona y recorre. Muy rápido en la práctica (`O(n log n)` promedio), **no estable**; peor caso `O(n²)` si el pivote es malo.
- **Heap Sort**: construye un **heap** y extrae en orden. `O(n log n)` en peor caso, in-place, **no estable**.

---

## 📊 Complejidad, estabilidad y memoria

| Algoritmo       | Mejor     | Promedio  | Peor      | Espacio extra | Estable | In-place |
|-----------------|-----------|-----------|-----------|---------------|---------|---------|
| Bubble Sort     | O(n)      | O(n²)     | O(n²)     | O(1)          | ✅      | ✅      |
| Insertion Sort  | O(n)      | O(n²)     | O(n²)     | O(1)          | ✅      | ✅      |
| Selection Sort  | O(n²)     | O(n²)     | O(n²)     | O(1)          | ❌      | ✅      |
| Merge Sort      | O(n log n)| O(n log n)| O(n log n)| O(n)          | ✅      | ❌      |
| Quick Sort      | O(n log n)| O(n log n)| O(n²)     | O(log n)\*    | ❌      | ✅      |
| Heap Sort       | O(n log n)| O(n log n)| O(n log n)| O(1)          | ❌      | ✅      |

---

## 🔎 ¿Cuándo usar cuál?

- **Listas pequeñas / casi ordenadas** → *Insertion Sort*
- **Rendimiento general en memoria limitada** → *Heap Sort*
- **Rendimiento práctico promedio** → *Quick Sort* (con buen pivote: aleatorizado o mediana de 3)
- **Rendimiento garantizado y estabilidad** → *Merge Sort*
- **Didácticos / muy simples** → *Bubble / Selection*

---

## 🧪 Ejemplos rápidos

**Insertion Sort**
```python
from insertion_sort import insertion_sort
print(insertion_sort([5, 2, 4, 6, 1, 3]))  # [1, 2, 3, 4, 5, 6]
```

**Quick Sort (interfaz típica)**

```python
from quick_sort import quick_sort
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr)   # in-place
print(arr)        # [1, 5, 7, 8, 9, 10]
```

**Merge Sort**

```python
from merge_sort import merge_sort
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # [3, 9, 10, 27, 38, 43, 82]
```

---

## 🧯 Consejos prácticos

* Para **datos enormes** que no caben en memoria: variantes de *Merge Sort externo*.
* Para evitar el peor caso de Quick Sort: **pivote aleatorio** o **mediana de tres**.
* Si necesitas **estable** e **in-place**, considera *Insertion* para subarreglos pequeños combinado con *Merge/Quick* (técnica “hybrid”, como **Timsort** en Python).

---

## 📚 Top recursos recomendados

1. **CLRS – *Introduction to Algorithms*** (capítulos de sorting)
2. **Algorithms, 4th Ed. – Sedgewick & Wayne** (visualizaciones y análisis)
3. **[VisuAlgo – Sorting](https://visualgo.net/en/sorting)** (animaciones interactivas)
4. **[GeeksforGeeks – Sorting](https://www.geeksforgeeks.org/sorting-algorithms/)** (implementaciones y variantes)

---

## 🙌 Créditos

Desarrollado con fines educativos ❤️ por [@luuiscc\_](https://github.com/luuuisc)
