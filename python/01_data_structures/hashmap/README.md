# 🗺️ Hashmap – Diccionarios implementados desde cero

Esta carpeta contiene una implementación personalizada de una estructura de datos tipo **HashMap** (también llamada tabla hash), junto con ejemplos de manejo de colisiones. En Python, la estructura `dict` es una tabla hash optimizada, pero aquí aprenderás cómo funciona internamente.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `custom_hashmap.py` | Implementación de un mapa hash simple desde cero |
| `collisions.py` | Ejemplos de colisiones y técnicas para resolverlas |

## ▶️ Cómo usar

Ejecuta cada script directamente para ver ejemplos de uso:

```bash
python collisions.py
python custom_hashmap.py
```

---

## 🧠 ¿Qué es un HashMap?

Un **HashMap** es una estructura de datos que almacena pares **clave → valor**, permitiendo operaciones como insertar, buscar y eliminar elementos en **tiempo constante promedio (`O(1)`)**.

Su funcionamiento se basa en tres pasos clave:

1. **Hashing**: convertir la clave en un número mediante una función hash.
2. **Indexación**: aplicar una operación (como módulo) para obtener una posición válida en un arreglo.
3. **Colisión**: resolver el caso donde dos claves tienen el mismo índice.

## 🔄 Operaciones típicas

| Operación | Descripción |
|----------|-------------|
| `put(clave, valor)` | Inserta o actualiza un par clave-valor |
| `get(clave)`        | Retorna el valor asociado a la clave |
| `remove(clave)`     | Elimina un par clave-valor del mapa |
| `contains(clave)`   | Retorna `True` si la clave existe |


## ⚠️ ¿Qué son las colisiones?

Una **colisión** ocurre cuando dos claves diferentes generan el mismo índice en la tabla. Esto es inevitable, y por eso existen estrategias para manejarlo:

### 🔹 Métodos comunes de resolución

| Técnica | Descripción |
|--------|-------------|
| Encadenamiento (chaining) | Cada celda del array contiene una lista de pares clave-valor |
| Direccionamiento abierto (open addressing) | Busca otra posición libre en la tabla (lineal, cuadrática, doble hashing) |

El archivo `collisions.py` te muestra cómo funcionan estas técnicas con ejemplos simples.


## 📈 Ejemplo de uso

```python
from custom_hashmap import HashMap

mapa = HashMap()
mapa.put("nombre", "Luis")
mapa.put("edad", 30)

print(mapa.get("nombre"))  # Luis
print(mapa.contains("edad"))  # True

mapa.remove("edad")
print(mapa.contains("edad"))  # False
```

## 🎯 ¿Por qué aprender esto si Python ya tiene dict?
- Te ayuda a entender cómo funciona dict internamente
- Fortalece tu comprensión de funciones hash y eficiencia algorítmica
- Es una habilidad clave en entrevistas técnicas y desafíos de programación

## 🧪 Recomendaciones
- Prueba tus propias claves para forzar colisiones
- Cambia el tamaño del array inicial para ver su efecto
- Añade soporte para redimensionamiento automático (como los dict reales)

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 