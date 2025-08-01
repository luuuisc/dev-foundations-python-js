# 📏 Estructuras de Datos Lineales

Esta carpeta contiene implementaciones básicas de **estructuras de datos lineales**: `array`, `queue` (cola) y `deque` (cola doble). Estas estructuras se caracterizan por tener un orden lineal en el almacenamiento y acceso a los elementos.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `array.py` | Implementación básica de un array dinámico (tipo lista) |
| `queue.py` | Implementación de una cola (FIFO – First In First Out) |
| `deque.py` | Implementación de una cola doble (Double-Ended Queue) |
| `stack.py`    | Implementación de una pila (LIFO – Last In First Out)   |

---
## ▶️ Cómo ejecutar

```bash
python array.py
python queue.py
python deque.py
python stack.py
```

## 🧠 ¿Qué es una estructura lineal?

Una estructura de datos lineal almacena los elementos de forma secuencial, uno tras otro. El acceso y recorrido de los elementos sigue un orden determinado, como:

- De izquierda a derecha (como una lista)
- De primero en entrar a primero en salir (como una cola)
- Con acceso por ambos extremos (como un deque)
- De último en entrar a primero en salir (como una pila)

---

## ⚙️ Operaciones comunes

| Operación            | Array | Queue | Deque | Stack |
|----------------------|-------|-------|-------|-------|
| Agregar al final     | ✅ `.append()`     | ✅ `.enqueue()`     | ✅ `.append_right()` | ✅ `.push()`  |
| Eliminar del inicio  | ✅ `pop(0)`        | ✅ `.dequeue()`     | ✅ `.pop_left()`     | ❌            |
| Agregar al inicio    | ❌ (ineficiente)   | ❌                  | ✅ `.append_left()`  | ❌            |
| Eliminar del final   | ✅ `.pop()`        | ❌                  | ✅ `.pop_right()`    | ✅ `.pop()`   |
| Acceso directo       | ✅ por índice      | ❌                  | ❌                   | ❌            |
---

## 📈 Ejemplos de uso

### 🔹 Array

```python
from array import CustomArray

arr = CustomArray()
arr.append(5)
arr.append(8)
print(arr.get(0))  # 5
```

### 🔹 Queue (Cola FIFO)

```python
from queue import Queue

cola = Queue()
cola.enqueue("A")
cola.enqueue("B")
print(cola.dequeue())  # A
```

### 🔹 Deque (Cola doble)

```python
from deque import Deque

dq = Deque()
dq.append_right(1)
dq.append_left(0)
print(dq.pop_right())  # 1
print(dq.pop_left())   # 0
```

### 🔹 Stack (Pila LIFO)

```python
from stack import Stack

pila = Stack()
pila.push(10)
pila.push(20)
print(pila.pop())  # 20
```

## 🌍 Aplicaciones comunes

| Estructura | Ejemplo de uso |
|------------|----------------|
| 📦 Array   | Almacenamiento de datos en listas ordenadas, manipulación de colecciones, implementación de otras estructuras (pilas, matrices). |
| 📤 Queue   | Gestión de tareas en colas de impresión, planificación de procesos en sistemas operativos, simulaciones en tiempo real. |
| 🔁 Deque   | Navegación adelante/atrás en navegadores, funcionalidades de undo/redo, buffers de datos en streaming o procesamiento por ventanas. |
| 🧱 Stack   | Algoritmos de retroceso (backtracking), deshacer/rehacer en editores, recorrido de árboles, evaluación de expresiones. |


## 🎯 ¿Por qué aprenderlas?
- Son la base para muchas otras estructuras más complejas.
- Aparecen en problemas de programación competitiva y entrevistas.
- Mejoran tu capacidad para elegir la estructura correcta en cada situación.

## 👀 ¿Qué es lo siguiente?

### 1. **Lista de Python (`lista = [1, 2, 3, 4]`)**
   - Es una estructura de datos **incorporada en Python** (built-in).
   - Es dinámica, puede almacenar elementos de **diferentes tipos** (enteros, strings, etc.).
   - Tiene muchos métodos útiles ya implementados (`append()`, `pop()`, `index()`, slicing, etc.).
   - Es muy eficiente y optimizada en Python.

   ```python
   lista = [1, 2, 3, 4]  # Lista normal de Python
   lista.append(5)        # Agrega un elemento al final
   print(lista[0])        # Accede al primer elemento (1)
   ```

### 2. **`CustomArray` (Arreglo personalizado)**
   - Es una **clase personalizada**.
   - Puede tener una implementación **limitada o diferente** a las listas de Python.
   - En el ejemplo, `CustomArray` tiene métodos como:
     - `append()` para agregar elementos.
     - `get(index)` para acceder a un elemento (en lugar de usar `arr[0]` como en las listas normales).
   - Puede estar diseñado para un **propósito específico**, como ser más eficiente en ciertas operaciones o tener restricciones (ejemplo: solo almacenar números).

   ```python
   from array import CustomArray  # Importa una clase personalizada

   arr = CustomArray()  # Crea una instancia de CustomArray
   arr.append(5)        # Agrega un elemento (similar a una lista)
   arr.append(8)
   print(arr.get(0))    # Imprime 5 (usa un método get() en lugar de [0])
   ```

### ⚡ Diferencia clave:
- **Lista de Python** es una estructura estándar, flexible y muy usada.
- **`CustomArray`** es una implementación personalizada, que puede tener un comportamiento diferente y métodos propios (como `get()` en lugar de `[ ]` para acceder a elementos).

### 🔍 ¿Por qué usar `CustomArray` en lugar de una lista normal?
- Si `CustomArray` está optimizado para un caso de uso específico (ejemplo: arreglos de tamaño fijo, operaciones matemáticas más rápidas).
- Si necesitas un control más estricto sobre cómo se almacenan los datos (ejemplo: solo permitir números enteros).

En la mayoría de los casos, **las listas normales de Python son suficientes**, pero a veces las estructuras personalizadas como `CustomArray` pueden ser útiles para necesidades específicas.

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 