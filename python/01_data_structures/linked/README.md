# 🔗 Linked Lists – Listas Enlazadas en Python

Esta carpeta contiene implementaciones manuales de las estructuras clásicas de **listas enlazadas**. Estas estructuras almacenan elementos en nodos que están conectados entre sí por referencias, en lugar de ocupar posiciones contiguas en memoria como los arrays.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `singly_linked_list.py` | Lista enlazada simple: cada nodo apunta al siguiente |
| `doubly_linked_list.py` | Lista doblemente enlazada: cada nodo apunta al anterior y al siguiente |
| `circular_linked_list.py` | Lista enlazada circular: el último nodo apunta al primero |

---

## ▶️ Cómo ejecutar

```bash
python singly_linked_list.py
python doubly_linked_list.py
python circular_linked_list.py
```


## 🧠 ¿Qué es una lista enlazada?

Una **lista enlazada** es una colección de nodos, donde cada nodo contiene:

- Un **valor**
- Una referencia (o puntero) al siguiente nodo

A diferencia de un array, no se necesita que los elementos estén contiguos en memoria, lo que permite inserciones y eliminaciones eficientes sin necesidad de mover todos los elementos.

---

## 🔄 Tipos de listas enlazadas

| Tipo | Características principales |
|------|-----------------------------|
| Lista simple | Unidireccional: solo puedes avanzar hacia adelante |
| Lista doble | Bidireccional: puedes avanzar y retroceder |
| Lista circular | El último nodo apunta al primero; útil para estructuras cíclicas |

---

## 🔧 Operaciones comunes

| Operación | Descripción |
|----------|-------------|
| `append(valor)` | Añadir un nodo al final |
| `prepend(valor)` | Añadir un nodo al inicio |
| `delete(valor)` | Eliminar el primer nodo que contenga el valor |
| `search(valor)` | Buscar un valor en la lista |
| `print_list()` | Imprimir los valores en orden |

---

## 📈 Ejemplo de uso

```python
from singly_linked_list import SinglyLinkedList

lista = SinglyLinkedList()
lista.append(10)
lista.append(20)
lista.prepend(5)
lista.print_list()  # 5 -> 10 -> 20
lista.delete(10)
lista.print_list()  # 5 -> 20
```

## 🌍 Aplicaciones comunes

| Estructura | Ejemplo de uso |
|------------|----------------|
| Lista simple (`singly linked list`) | Implementación de pilas, colas, buffers de datos, navegación secuencial en archivos. |
| Lista doble (`doubly linked list`) | Navegadores (botones adelante/atrás), historial de acciones (undo/redo), listas ordenadas con acceso bidireccional. |
| Lista circular (`circular linked list`) | Listas de reproducción (loop), planificación por turnos, sistemas embebidos (timers circulares), controladores de juegos. |

## ⚖️ Diferencias entre `list` de Python y listas enlazadas

| Característica | `list` (array dinámico) | Lista enlazada |
|----------------|--------------------------|----------------|
| Estructura interna | Bloques contiguos en memoria | Nodos conectados por referencias |
| Acceso por índice | ✅ Muy rápido (`O(1)`) | ❌ Lento (`O(n)`), recorrido secuencial |
| Inserción/eliminación al final | ✅ Muy eficiente (`O(1)` amortizado) | ✅ Eficiente si se tiene referencia al último nodo |
| Inserción/eliminación en medio/inicio | ❌ Costosa (`O(n)`) | ✅ Rápida (`O(1)`) si se tiene el nodo anterior |
| Uso de memoria | Más compacto, mejor para acceso rápido | Mayor overhead por los punteros en cada nodo |
| Ideal para | Acceso rápido por posición | Inserciones/eliminaciones frecuentes y dinámicas |

🔎 En resumen:
- Usa `list` si necesitas acceso rápido por índice o tamaño fijo/moderado.
- Usa **listas enlazadas** si haces muchas inserciones/eliminaciones, especialmente en medio o al inicio.

## 🎯 ¿Por qué aprender listas enlazadas?
- Te enseñan a manejar punteros/referencias y lógica recursiva
- Son la base para estructuras más complejas como árboles o grafos
- Aparecen frecuentemente en entrevistas técnicas y exámenes de algoritmos

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 
