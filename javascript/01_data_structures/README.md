# 🧱 Estructuras de Datos en JavaScript

Implementaciones **desde cero** en **JavaScript (ES2023/Node ≥18)** para entender cómo funcionan por dentro las estructuras más usadas. El objetivo es **aprender la idea, la API y la complejidad**, y luego revisar ejemplos mínimos.

Cada subcarpeta incluye:

* Breve teoría y **API** de la estructura
* Implementación propia (sin depender de librerías externas)
* Ejemplos prácticos y casos de uso
* Complejidades Big-O y buenas prácticas
* Indicaciones de prueba con Jest

> Filosofía: primero entender el “por qué”, después ver el “cómo” con código breve.

---

## 📑 Índice de subcarpetas

| Carpeta                  | Qué cubre                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------- |
| [`linear/`](./linear/)   | **Stack**, **Queue**, **Deque** (operaciones O(1) amortizadas)                        |
| [`linked/`](./linked/)   | **Singly**, **Doubly**, **Circular** (nodos, punteros, costo de inserciones/borrados) |
| [`tree/`](./tree/)       | **Binary Tree**, **BST**, recorridos (**pre/in/post/level**)                          |
| [`graph/`](./graph/)     | Representaciones (**lista/ matriz**), **BFS/DFS**, nociones de conectividad           |
| [`hashmap/`](./hashmap/) | **Hash Map**: función de hash, **chaining** y **open addressing**                     |
| [`heap/`](./heap/)       | **Min-Heap / Max-Heap**, **Priority Queue** (inserción y extracción en O(log n))      |
| [`trie/`](./trie/)       | **Trie** de prefijos para cadenas (búsqueda y autocompletado)                         |

---

## 🎯 Objetivos de esta sección

* Comprender la **lógica interna** de cada estructura.
* Diseñar **APIs claras** (métodos, invariantes, errores).
* Relacionar la estructura con su **complejidad temporal y espacial**.
* Practicar para **entrevistas técnicas** y retos de código.

---

## 🧭 Convenciones y organización

* **ES Modules** por defecto (`export`/`import`).
* Una estructura = **una clase + un README corto** con:

  * *Idea clave* (intuición + diagrama simple)
  * *API mínima* (métodos públicos)
  * *Complejidad* (insert, delete, search, peek, etc.)
  * *Casos borde* (underflow/overflow, colisiones, valores repetidos…)
  * *Ejemplos* (2–3 líneas de uso)
* Nombres sugeridos de archivos:

```
javascript/01_data_structures/
├─ linear/
│  ├─ stack.js           # push, pop, peek, size, isEmpty
│  ├─ queue.js           # enqueue, dequeue, peek, size
│  ├─ deque.js           # addFront, addBack, removeFront, removeBack
│  └─ README.md
├─ linked/
│  ├─ singly_linked_list.js
│  ├─ doubly_linked_list.js
│  ├─ circular_linked_list.js
│  └─ README.md
├─ tree/
│  ├─ binary_tree.js     # nodos + recorridos
│  ├─ bst.js             # insert, search, delete (3 casos)
│  └─ README.md
├─ graph/
│  ├─ adjacency_list.js  # addVertex, addEdge, neighbors
│  ├─ bfs.js
│  ├─ dfs.js
│  └─ README.md
├─ hashmap/
│  ├─ hash_map_chaining.js
│  ├─ hash_map_open_addressing.js
│  └─ README.md
├─ heap/
│  ├─ min_heap.js
│  ├─ max_heap.js
│  ├─ priority_queue.js
│  └─ README.md
└─ trie/
   ├─ trie.js            # insert, search, startsWith, delete (opcional)
   └─ README.md
```

---

## 🧪 Cómo probar (rápido)

* Ejecuta ejemplos directos:

```bash
node javascript/01_data_structures/linear/stack_demo.js
```

* Tests con **Jest** (en `javascript/04_testing/`):

```bash
npm i
npm test -- linear
# o por archivo:
npx jest linear/stack.test.js
```

> Tip: cada clase exporta la estructura y, si aplica, una **función fábrica** para crearla con datos iniciales (útil en tests).

---

## 🧠 Qué debes mirar en cada estructura (checklist)

1. **Invariante**: ¿qué debe mantenerse siempre cierto?
2. **API mínima**: ¿cuáles son 3–5 métodos que la hacen útil?
3. **Complejidad**: ¿qué operaciones son O(1), O(log n), O(n)?
4. **Errores**: ¿qué pasa si saco de una estructura vacía?
5. **Uso real**: ¿en qué problemas brilla esta estructura?

---

## 📌 Resumen de complejidades (guía rápida)

> *Valores típicos; la implementación exacta puede variar.*

| Estructura                | Insertar |   Borrar | Buscar/Acceder | Comentario                                |
| ------------------------- | -------: | -------: | -------------: | ----------------------------------------- |
| **Stack / Queue / Deque** |     O(1) |     O(1) |    O(1) (peek) | Amortizado en arrays dinámicos            |
| **Linked List (S/D/C)**   |   O(1)\* |   O(1)\* |           O(n) | \*si tienes referencia a nodo/cabeza/cola |
| **BST (no balanceado)**   |     O(h) |     O(h) |           O(h) | En peor caso h≈n                          |
| **Heap (binario)**        | O(log n) | O(log n) |    O(1) (peek) | Priority Queue clásica                    |
| **Hash Map**              | O(1) avg | O(1) avg |       O(1) avg | Depende de hash/resize/colisiones         |
| **Trie**                  |     O(L) |     O(L) |           O(L) | L = longitud de la clave                  |

---

## 🧩 Ejemplos mínimos (solo para fijar ideas)

> Revisa los archivos `.js` para la implementación completa.

**Stack (API mental)**

```js
// push(x), pop(), peek(), size(), isEmpty()
```

**Min-Heap (operaciones clave)**

```txt
siftUp(index)   // restaurar propiedad tras insertar
siftDown(index) // restaurar tras extraer mínimo
```

**Hash Map (ideas clave)**

* Función de **hash** + normalización de índice.
* **Chaining** (lista de pares en cada bucket) o **open addressing** (lineal/cuadrático).

---

## ✅ Buenas prácticas en JS para EDD

* Prefiere **ESM** y clases pequeñas con responsabilidades claras.
* Evita filtrar/ordenar en cada operación; conserva el **invariante**.
* Documenta pre/postcondiciones (ej. “lanza Error si la estructura está vacía”).
* En tests, cubre **casos borde** (vacío, duplicados, deletes encadenados).
* Mantén **interfaz uniforme** (p. ej., `size()` e `isEmpty()` en todas).

---

## 🚀 Ruta sugerida de estudio

1. `linear/` → 2. `linked/` → 3. `heap/` → 4. `tree/`(BST) → 5. `hashmap/` → 6. `trie/` → 7. `graph/` (BFS/DFS primero).
   Cierra cada bloque resolviendo 2–3 problemas donde esa estructura sea natural.

---

## ✍️ Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc\_](https://github.com/luuuisc)
