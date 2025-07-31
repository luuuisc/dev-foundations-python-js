# 📘 00_intro_basics – Fundamentos de Python

Esta carpeta contiene los conceptos más básicos del lenguaje Python, ideales para quienes se inician o necesitan repasar fundamentos antes de abordar temas más complejos.

## 📑 Índice

- [Archivos incluidos](#archivos-incluidos)
- [Recomendaciones](#️-recomendaciones)
- [01. Variables y tipos de datos](#-variables-y-tipos-de-datos-en-python)
- [02. Entrada y salida](#-entrada-y-salida-en-python-input-y-print)
- [03. Condicionales](#-condicionales-if-elif-else)
- [04. Bucles](#-bucles-for-y-while)
- [05. Funciones](#-funciones-en-python)
- [06. Listas, diccionarios y sets](#-estructuras-de-datos-básicas-list-dict-set)
- [07. Módulos e imports](#-módulos-e-imports)

## Archivos incluidos

| Archivo | Tema |
|--------|------|
| `01_hello_world.py` | Primer script en Python e impresión en consola |
| `02_variables_types.py` | Declaración de variables y tipos de datos |
| `03_input_output.py` | Entrada del usuario y salida formateada |
| `04_conditionals.py` | Condicionales `if`, `elif`, `else` |
| `05_loops.py` | Bucles `for` y `while` |
| `06_functions.py` | Definición y uso de funciones |
| `07_list_dict_set.py` | Estructuras de datos básicas (`list`, `dict`, `set`) |
| `08_modules_imports.py` | Importación de módulos y uso de funciones externas |

---

## 🛠️ Recomendaciones

- Usa `print()` para depurar en tus primeras prácticas.
- Usa comentarios para explicar tu código, incluso si solo lo usas tú.
- Ejecuta los archivos individualmente con:

```bash
python nombre_archivo.py
```

---

# 📘 Variables y tipos de datos en Python

## 🧠 ¿Qué es una variable?

Una variable es un espacio en memoria que guarda un valor. En Python, las variables no necesitan ser declaradas con un tipo explícito: el lenguaje es dinámicamente tipado, lo que significa que puedes asignar cualquier tipo de valor sin definir su tipo previamente.

```python
nombre = "Ana"
edad = 25
pi = 3.14
```

## 🧾 Reglas para nombrar variables
- Deben comenzar con una letra o guion bajo (_), nunca con un número.
- Solo pueden contener letras, números y guiones bajos.
- Python es sensible a mayúsculas y minúsculas (Nombre ≠ nombre).
- Usa snake_case como convención para mejorar la legibilidad.

```python
usuario_activo = True      # ✅ Correcto
UsuarioActivo = True       # ⚠️ Permitido, pero estilo de clase
1usuario = "Luis"          # ❌ Incorrecto
```

## 📦 Tipos de datos principales en Python


| Tipo         | Ejemplo            | Descripción breve                          |
|--------------|--------------------|--------------------------------------------|
| `int`        | `x = 10`           | Números enteros                            |
| `float`      | `pi = 3.14`        | Números decimales (punto flotante)         |
| `str`        | `"Hola"`           | Cadenas de texto                           |
| `bool`       | `True / False`     | Booleanos (valores lógicos)                |
| `list`       | `[1, 2, 3]`        | Lista ordenada, mutable                    |
| `tuple`      | `(1, 2, 3)`        | Lista ordenada, **inmutable**              |
| `set`        | `{1, 2, 3}`        | Colección desordenada, **sin duplicados**  |
| `dict`       | `{"a": 1, "b": 2}` | Diccionario con pares clave-valor          |
| `NoneType`   | `None`             | Ausencia de valor                          |

## 🔍 Ver el tipo de una variable

Usa la función integrada type() para inspeccionar el tipo de cualquier variable:

```python
nombre = "Luis"
print(type(nombre))  # <class 'str'>
```

## 💡 Buenas prácticas
- Usa nombres descriptivos (total_puntos, nombre_usuario)
- Evita nombres genéricos o de una letra (x, temp, data)
- Define constantes en mayúsculas: PI = 3.1416
- Usa f-strings para imprimir valores de forma legible:

```python
nombre = "Ana"
print(f"Bienvenida, {nombre}")
```

# 📥 Entrada y salida en Python (`input()` y `print()`)

## 🖋️ print() – Mostrar información en pantalla

La función print() se usa para mostrar texto o valores en consola.

```python
print("Hola, mundo")
```

Puedes imprimir múltiples valores separados por comas:

```python
nombre = "Luis"
edad = 25
print("Nombre:", nombre, "- Edad:", edad)
```

O usar f-strings para una impresión más elegante:

```python
print(f"{nombre} tiene {edad} años.")
```
## ⌨️ input() – Capturar datos del usuario

La función input() permite obtener datos desde la consola como cadena de texto (str):

```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}!")
```

Para convertir la entrada a otro tipo:

```python
edad = int(input("¿Cuántos años tienes? "))
```

🔎 Importante: Siempre que uses input(), considera validar o convertir el tipo para evitar errores.


# 🔁 Condicionales if, elif, else

Las condicionales permiten que el programa tome decisiones según ciertas condiciones.

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad == 17:
    print("Casi eres mayor de edad")
else:
    print("Eres menor de edad")
```

- Puedes encadenar condiciones usando and, or, not.
- Python usa indentación obligatoria (4 espacios) para definir bloques.

# 🔄 Bucles for y while

## 🔁 for

Usado para recorrer elementos de listas, cadenas u objetos iterables:

```python
for letra in "Python":
    print(letra)
```

También puedes usar range() para generar secuencias numéricas:

```python
for i in range(5):
    print(i)
```

## ♻️ while

Repite un bloque mientras una condición sea verdadera:

```python
contador = 0
while contador < 3:
    print("Hola")
    contador += 1
```

🧠 Usa `break` para salir anticipadamente de un bucle y continue para saltar una iteración.


# 🧩 Funciones en Python

Las funciones agrupan bloques de código reutilizable. Se definen con la palabra clave def.

```python
def saludar(nombre):
    print(f"Hola, {nombre}!")
```

Se puede usar:

```python
saludar("Luis")
```

También pueden devolver valores con return:

```python
def cuadrado(x):
    return x ** 2
```

🔎 Las funciones mejoran la claridad, reducen errores y permiten dividir el código en partes manejables.

# 🗃️ Estructuras de datos básicas (list, dict, set)

## 🔢 Listas (list)

Colección ordenada y modificable.

```python
frutas = ["manzana", "plátano", "pera"]
print(frutas[0])  # manzana
```

Puedes agregar con `.append()` y recorrer con for.

## 🔑 Diccionarios (dict)

Pares clave-valor:

```python
persona = {"nombre": "Luis", "edad": 30}
print(persona["nombre"])  # Luis
```

## 🎯 Conjuntos (set)

Colecciones sin duplicados y sin orden garantizado.

```python
numeros = {1, 2, 3, 2}
print(numeros)  # {1, 2, 3}
```

# 📦 Módulos e imports

Python permite reutilizar código separándolo en módulos.

➕ Importar funciones

```python
import math
print(math.sqrt(16))  # 4.0
```

O bien:

```python
from math import sqrt
print(sqrt(25))  # 5.0
```

Puedes también crear tus propios módulos (archivos .py) y usarlos con import.
