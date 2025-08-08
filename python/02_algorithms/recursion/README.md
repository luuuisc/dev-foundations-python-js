# 🔄 Recursión

La **recursión** es una técnica de programación en la que una función se llama a sí misma directa o indirectamente para resolver un problema.  
Se utiliza cuando un problema puede dividirse en **subproblemas más pequeños** de la misma naturaleza, resolviendo cada uno de forma similar.

---

## 📂 Archivos incluidos

| Archivo         | Descripción |
|-----------------|-------------|
| `factorial.py`  | Cálculo del factorial de un número usando recursión |
| `fibonacci.py`  | Cálculo del n-ésimo número de la serie de Fibonacci |
| `palindrome.py` | Verificación de si una cadena es un palíndromo usando recursión |

---

## 🧠 Teoría general de recursión

Para que un algoritmo recursivo funcione correctamente debe cumplir con:
1. **Caso base** – Condición que detiene la recursión y devuelve un resultado directo.
2. **Caso recursivo** – Llamada a la misma función con un problema más pequeño o reducido.
3. **Progreso hacia el caso base** – Asegurar que cada llamada reduce el problema.

La recursión es poderosa, pero puede ser ineficiente si no se maneja correctamente, ya que:
- Puede consumir mucha memoria en la pila de llamadas.
- Puede recalcular subproblemas múltiples veces (problema común en *Fibonacci* sin memoización).

---

## 📜 Explicación teórica de los algoritmos

### 1. Factorial
El factorial de un número `n` (denotado como `n!`) es el producto de todos los enteros positivos hasta `n`.

**Definición matemática:**

```
n! = n × (n-1)!
0! = 1
```

**Recursivo:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Complejidad: **O(n)** tiempo y **O(n)** espacio por las llamadas recursivas.

---

### 2. Fibonacci

La secuencia de Fibonacci se define como:

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
```

**Recursivo simple:**

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Complejidad: **O(2^n)** tiempo sin optimización. Con memoización se reduce a **O(n)**.

---

### 3. Palíndromo

Una cadena es un palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.

**Idea recursiva:**

* Comparar el primer y último carácter.
* Si son iguales, verificar recursivamente la subcadena central.
* Caso base: cadena vacía o de un solo carácter → es palíndromo.

```python
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
```

Complejidad: **O(n)** tiempo, **O(n)** espacio por la pila.

---

## 📊 Complejidad esperada

| Algoritmo  | Temporal      | Espacial | Notas                                  |
| ---------- | ------------- | -------- | -------------------------------------- |
| Factorial  | O(n)          | O(n)     | Una llamada por cada decremento de `n` |
| Fibonacci  | O(2^n) → O(n) | O(n)     | Mejorar con memoización/tabulación     |
| Palíndromo | O(n)          | O(n)     | La pila de llamadas crece linealmente  |

---

## 🌍 Aplicaciones reales

| Algoritmo  | Aplicaciones                                                                              |
| ---------- | ----------------------------------------------------------------------------------------- |
| Factorial  | Combinatoria, probabilidad, análisis de algoritmos                                        |
| Fibonacci  | Modelado de crecimiento, algoritmos de optimización, estructuras como el *Fibonacci Heap* |
| Palíndromo | Procesamiento de lenguaje natural, bioinformática (detección de secuencias), criptografía |

---

## 📚 Top 5 recursos recomendados

1. **[Recursion - GeeksforGeeks](https://www.geeksforgeeks.org/recursion/)** – Introducción completa con ejemplos.
2. **[MIT OpenCourseWare - Recursion](https://ocw.mit.edu/)** – Lecciones en video y ejercicios.
3. **[Think Python - Recursion](https://greenteapress.com/thinkpython2/html/thinkpython2009.html)** – Capítulo de recursión en un libro gratuito.
4. **Libro: "Introduction to Algorithms" (CLRS)** – Capítulos iniciales sobre recursión y análisis.
5. **[Python Recursion - Real Python](https://realpython.com/python-recursion/)** – Ejemplos prácticos y buenas prácticas.

---

## 🙌 Créditos

Desarrollado con fines educativos ❤️ por [@luuiscc\_](https://github.com/luuuisc)

