# ➗ Algoritmos Matemáticos

Esta carpeta contiene implementaciones de **algoritmos matemáticos fundamentales**, útiles para resolver problemas numéricos de forma eficiente. Estos métodos son la base de muchas áreas como criptografía, teoría de números, optimización y análisis computacional.

---

## 📂 Archivos incluidos

| Archivo                        | Descripción |
|--------------------------------|-------------|
| `fast_exponentiation.py`       | Exponenciación rápida (potenciación binaria) para calcular potencias en tiempo logarítmico |
| `gcd.py`                       | Cálculo del Máximo Común Divisor (MCD) usando el algoritmo de Euclides |
| `sieve_of_eatosthenes.py`      | Criba de Eratóstenes para encontrar todos los números primos hasta un límite dado |

---

## 🧠 Descripción breve de los algoritmos

1. **Exponenciación rápida (Fast Exponentiation)**  
   - Calcula potencias grandes en **O(log n)** multiplicaciones usando descomposición binaria.
   - Muy utilizada en **criptografía** y **matemática modular**.

2. **Máximo Común Divisor (GCD)**  
   - Algoritmo de Euclides para encontrar el divisor común más grande entre dos números.

3. **Criba de Eratóstenes**  
   - Método eficiente para generar números primos menores o iguales a un número `n`.

---

## ⏱️ Complejidad esperada

| Algoritmo                 | Temporal            | Espacial | Notas |
|---------------------------|--------------------|----------|-------|
| Fast Exponentiation       | O(log n)           | O(1)     | Útil en operaciones modulares |
| GCD (Euclides)            | O(log min(a, b))   | O(1)     | Una de las funciones más rápidas en matemáticas |
| Sieve of Eratosthenes     | O(n log log n)     | O(n)     | Muy eficiente para grandes `n` |

---

## 🧪 Ejemplos rápidos

**Exponenciación rápida**
```python
from fast_exponentiation import power
print(power(2, 10))  # 1024
````

**Máximo Común Divisor**

```python
from gcd import gcd
print(gcd(48, 18))  # 6
```

**Criba de Eratóstenes**

```python
from sieve_of_eatosthenes import sieve
print(sieve(30))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## 🌍 Aplicaciones reales

| Área                   | Ejemplo                                                           |
| ---------------------- | ----------------------------------------------------------------- |
| Criptografía           | RSA, Diffie–Hellman (uso de potencias modulares y primos grandes) |
| Procesamiento de datos | Normalización de fracciones con MCD                               |
| Ciencia e ingeniería   | Simulaciones numéricas, generación de primos para tests           |

---

## 📚 Top 5 recursos recomendados

1. **[Number Theory - GeeksforGeeks](https://www.geeksforgeeks.org/number-theory-competitive-programming/)** – Conceptos clave de teoría de números.
2. **[Modular Arithmetic and Fast Exponentiation - CP Algorithms](https://cp-algorithms.com/)** – Guía clara y práctica.
3. **[Greatest Common Divisor - Brilliant.org](https://brilliant.org/wiki/greatest-common-divisor/)** – Explicación visual y demostraciones.
5. **Libro: "Elementary Number Theory" - David M. Burton** – Referencia completa de teoría de números.

---

## 🙌 Créditos

Desarrollado con fines educativos ❤️ por [@luuiscc\_](https://github.com/luuuisc)
