# 02_variables_types.py
"""
Variables y tipos de datos en Python.

Este script muestra cómo declarar variables de distintos tipos,
cómo comprobar su tipo y algunas recomendaciones de buenas prácticas.
"""

# 1. Variables numéricas
entero = 10                     # int
decimal = 3.14                  # float
numero_grande = 1_000_000       # separadores visuales

# 2. Variables de texto
nombre = "Luis"
saludo = f"Hola, {nombre}"      # f-strings
parrafo = """Este es un
texto multilínea."""

# 3. Booleanos
activo = True
completado = False

# 4. Colecciones básicas
lista = [1, 2, 3, 4]            # list
tupla = (1, 2, 3)               # tuple (inmutable)
conjunto = {1, 2, 2, 3}         # set (únicos)
diccionario = {"nombre": "Luis", "edad": 25}  # dict

# 5. Tipo None (ausencia de valor)
nada = None

# 6. Mostrar tipo de variable con type()
print("El tipo de 'entero' es:", type(entero))
print("El tipo de 'saludo' es:", type(saludo))
print("El tipo de 'conjunto' es:", type(conjunto))
print("El tipo de 'nada' es:", type(nada))

# Buenas prácticas
nombre_usuario = "maria"        # snake_case recomendado
PI = 3.14159                    # mayúsculas para constantes