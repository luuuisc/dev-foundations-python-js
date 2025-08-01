# 🌳 Árboles – Estructuras Jerárquicas en Python

Esta carpeta contiene implementaciones fundamentales de **estructuras de árboles**, una de las estructuras más importantes y versátiles en informática. Los árboles permiten organizar datos de forma jerárquica y son la base de muchas estructuras más complejas.

---

## 📂 Archivos incluidos

| Archivo | Descripción |
|---------|-------------|
| `binary_tree.py` | Árbol binario básico (cada nodo tiene hasta dos hijos) |
| `binary_Search_tree.py` | Árbol binario de búsqueda (BST), con inserción y búsqueda ordenada |
| `AVL_tree.py` | Árbol auto-balanceado AVL: mantiene el árbol equilibrado automáticamente |
| `traversal.py` | Implementaciones de recorridos: inorden, preorden, postorden y BFS |

---

## ▶️ Cómo ejecutar

```bash
python binary_tree.py
python binary_Search_tree.py
python AVL_tree.py
python traversal.py
```

## 🧠 ¿Qué es un árbol?

Un **árbol** es una estructura jerárquica compuesta por nodos conectados. Tiene:

- Un **nodo raíz** (el punto de partida)
- **Nodos hijos** (conexiones descendentes)
- Opcionalmente, **hojas** (nodos sin hijos)

Un **árbol binario** limita cada nodo a tener como máximo **dos hijos**: izquierdo y derecho.

---

## 🌲 Tipos de árboles implementados

| Tipo de árbol | Descripción |
|---------------|-------------|
| Árbol binario | Cada nodo tiene como máximo dos hijos |
| Árbol binario de búsqueda (BST) | El hijo izquierdo es menor que el nodo, el derecho es mayor |
| Árbol AVL | BST auto-balanceado: mantiene la diferencia de alturas ≤ 1 |
| Árbol completo/balanceado | (No implementado aquí) Todos los niveles llenos, excepto posiblemente el último |

---

## 🔁 Recorridos comunes (`traversal.py`)

| Tipo | Orden |
|------|-------|
| Inorden (`inorder`) | izquierda → nodo → derecha |
| Preorden (`preorder`) | nodo → izquierda → derecha |
| Postorden (`postorder`) | izquierda → derecha → nodo |
| Por niveles (`BFS`) | de arriba hacia abajo, nivel por nivel |

---

## 📈 Ejemplo de uso

```python
from binary_Search_tree import BST

arbol = BST()
arbol.insert(50)
arbol.insert(30)
arbol.insert(70)

print(arbol.search(30))  # True
print(arbol.search(90))  # False
arbol.inorder()          # [30, 50, 70]
```

## 🌍 Aplicaciones comunes

| Estructura | Ejemplo de uso |
|------------|----------------|
| 🌿 Árbol binario | Representación de expresiones matemáticas, árboles de decisión en inteligencia artificial, jerarquías simples. |
| 📚 Árbol binario de búsqueda (BST) | Implementación de diccionarios, bases de datos ordenadas, motores de búsqueda internos. |
| ⚖️ Árbol AVL | Búsqueda, inserción y eliminación con eficiencia garantizada (`O(log n)`), ideal para estructuras que requieren balance constante. |
| 🔁 Recorridos (DFS/BFS) | Análisis sintáctico en compiladores, motores de juegos, estructuras del DOM en navegadores, exportación estructurada de datos. |

## 🎯 ¿Por qué aprender árboles?
- Son fundamentales para el diseño de algoritmos
- Aparecen en estructuras clave como heaps, tries, grafos, DOM, etc.
- Dominarlos mejora tu rendimiento en entrevistas técnicas y programación competitiva

## 🙌 Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 
