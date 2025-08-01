# 🔤 Trie – Árbol de Prefijos

Esta carpeta contiene la implementación de un **Trie**, también conocido como **árbol de prefijos** o **árbol digital**. Es una estructura de datos especializada en almacenar cadenas de texto, especialmente útil para búsquedas rápidas de palabras, autocompletado y correctores ortográficos.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `trie.py` | Implementación de un Trie con inserción y búsqueda de palabras |


## ▶️ Cómo ejecutar

```bash
python trie.py
```

Modifica el archivo para probar más palabras, prefijos o casos límite.

---

## 🧠 ¿Qué es un Trie?

Un **Trie** es una estructura de árbol en la que cada nodo representa un **carácter** de una palabra. Las palabras que comparten prefijos también comparten nodos, lo que lo hace muy eficiente para operaciones de texto.

Por ejemplo, las palabras `perro`, `pera` y `pelota` compartirán las ramas `p → e`.

---

## 🔄 Operaciones comunes

| Operación | Descripción | Complejidad |
|-----------|-------------|-------------|
| `insert(palabra)` | Inserta una palabra en el trie | `O(m)` donde `m` es la longitud de la palabra |
| `search(palabra)` | Verifica si una palabra existe en el trie | `O(m)` |
| `starts_with(prefijo)` | Verifica si alguna palabra comienza con el prefijo dado | `O(m)` |

---

## 📈 Ejemplo de uso

```python
from trie import Trie

diccionario = Trie()
diccionario.insert("gato")
diccionario.insert("galaxia")

print(diccionario.search("gato"))       # True
print(diccionario.search("gal"))        # False
print(diccionario.starts_with("gal"))   # True
```

¡Claro! Aquí tienes la tabla de aplicaciones comunes de los Tries en formato Markdown (.md), lista para que la pegues directamente en tu README.md:

## 🌍 Aplicaciones comunes

| Aplicación                  | Descripción breve |
|-----------------------------|-------------------|
| 🔍 Autocompletado           | Sugerencias mientras se escribe una palabra (e.g. buscadores, IDEs) |
| 📝 Corrector ortográfico    | Detección y sugerencia de palabras mal escritas |
| 📱 Búsqueda predictiva      | Teclados virtuales que proponen palabras mientras se escribe |
| 🔐 Filtrado de contenido    | Detección rápida de palabras prohibidas en chats o redes sociales |
| 🧠 Reconocimiento de patrones | Procesamiento de texto y coincidencia de cadenas |
| 📦 Compresión de texto      | Algoritmos como LZ-trie y almacenamiento compacto de palabras |

## 🎯 ¿Por qué aprender sobre Tries?
- Son la estructura ideal para procesar texto carácter por carácter
- Permiten búsquedas más rápidas que otras estructuras cuando hay muchos prefijos en común
- Aparecen en entrevistas, algoritmos de texto y compresión

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 
