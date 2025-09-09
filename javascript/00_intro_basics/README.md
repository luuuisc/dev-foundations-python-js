# 📘 Fundamentos de JavaScript

Guía breve para entender **qué pasa y por qué** en JavaScript. Código mínimo, ideas claras. Ideal para repasar antes de estructuras de datos, algoritmos o DOM.

## 📑 Índice

* [Archivos incluidos](#archivos-incluidos)
* [Cómo usar esta carpeta](#cómo-usar-esta-carpeta)
* [01. Variables y tipos](#01-variables-y-tipos)
* [02. Entrada y salida (Node)](#02-entrada-y-salida-node)
* [03. Condicionales](#03-condicionales)
* [04. Bucles](#04-bucles)
* [05. Funciones](#05-funciones)
* [06. Arrays/Objects/Set/Map](#06-arraysobjectssetmap)
* [07. Módulos (ESM)](#07-módulos-esm)
* [08. Ámbito, hoisting y closures](#08-ámbito-hoisting-y-closures)
* [09. Errores](#09-errores)
* [10. Asincronía](#10-asincronía)
* [Buenas prácticas rápidas](#buenas-prácticas-rápidas)
* [Glosario mínimo](#glosario-mínimo)

---

## Archivos incluidos

| Archivo                          | Propósito                                      |
| -------------------------------- | ---------------------------------------------- |
| `01_hello_world.js`              | Primer script y `console.log`                  |
| `02_variables_types.js`          | `var` vs `let` vs `const`, tipos, `typeof`     |
| `03_input_output.js`             | Entrada con `readline/promises` en Node        |
| `04_conditionals.js`             | `if/else`, `switch`, truthy/falsy              |
| `05_loops.js`                    | `for`, `while`, `for…of`, `for…in`             |
| `06_functions.js`                | Funciones, arrow, `this`, rest/spread          |
| `07_arrays_objects_sets_maps.js` | Métodos clave de arrays, objetos, `Set`, `Map` |
| `08_modules_imports.mjs`         | ES Modules (`export`/`import`)                 |
| `09_scope_hoisting_closures.js`  | Ámbitos y closures                             |
| `10_error_handling.js`           | `try/catch/finally` y errores propios          |
| `11_async_basics.js`             | Promesas y `async/await`                       |

---

## Cómo usar esta carpeta

* Requisitos: **Node.js ≥ 18**.
* Ejecuta ejemplos de forma individual:

  ```bash
  node 01_hello_world.js
  ```
* El objetivo es **leer primero la teoría de cada sección** y luego abrir el archivo correspondiente para ver un ejemplo mínimo.

---

## 01. Variables y tipos

**Qué entender**

* JS es **dinámico** (el tipo puede cambiar) y **con coerción** (conversión implícita).
* Usa **`const` por defecto**, `let` si vas a reasignar, evita `var`.
* Tipos primitivos: `number`, `string`, `boolean`, `null`, `undefined`, `bigint`, `symbol`.
  De referencia: `object` (incluye arrays, funciones, mapas, etc.).

**Micro-ejemplo**

```js
const nombre = "Ana";
let puntos = 10;
console.log(typeof nombre); // "string"
console.log(typeof null);   // "object" (quirk histórico)
```

---

## 02. Entrada y salida (Node)

**Qué entender**

* Salida: `console.log`.
* Entrada sencilla en terminal con `readline/promises`.
* Todo input llega como **string**; conviértelo tú.

**Micro-ejemplo**

```js
import readline from "node:readline/promises";
import { stdin, stdout } from "node:process";

const rl = readline.createInterface({ input: stdin, output: stdout });
const edad = Number(await rl.question("Edad: "));
console.log(edad >= 18 ? "Mayor" : "Menor");
rl.close();
```

---

## 03. Condicionales

**Qué entender**

* `===`/`!==` evitan sorpresas de coerción.
* Valores **falsy**: `0`, `""`, `null`, `undefined`, `NaN`, `false`.
* `switch` es útil para múltiples casos del mismo valor.

**Micro-ejemplo**

```js
const v = "";
if (!v) console.log("falsy");
```

---

## 04. Bucles

**Qué entender**

* `for` y `while` son generales;
  `for…of` recorre **valores**; `for…in` recorre **claves** (objetos).
* Usa `break`/`continue` con moderación.

**Micro-ejemplo**

```js
for (const ch of "JS") console.log(ch);
```

---

## 05. Funciones

**Qué entender**

* Declaradas vs **arrow**. Las arrow **no** rebindean `this`.
* Parámetros por defecto y **rest/spread** facilitan APIs limpias.

**Micro-ejemplo**

```js
const sum = (...xs) => xs.reduce((a,b)=>a+b,0);
console.log(sum(1,2,3)); // 6
```

---

## 06. Arrays/Objects/Set/Map

**Qué entender**

* Arrays: transformaciones con `map`, `filter`, `reduce`.
* Objetos: acceso por punto o por llave.
* `Set` elimina duplicados; `Map` tiene llaves de cualquier tipo.

**Micro-ejemplo**

```js
const s = new Set([1,1,2,3]);  // {1,2,3}
const m = new Map([["a",1],["b",2]]);
```

---

## 07. Módulos (ESM)

**Qué entender**

* ESM: `export` / `import`.
* En Node: usa `.mjs` o `type: "module"` en `package.json`.

**Micro-ejemplo**

```js
// math.mjs
export const sum = (a,b)=>a+b;
// main.mjs
import { sum } from "./math.mjs"; console.log(sum(2,3));
```

---

## 08. Ámbito, hoisting y closures

**Qué entender**

* Ámbitos: global, función y **bloque** (`let`/`const`).
* Hoisting: las **declaradas** se “elevan”; las arrow **no**.
* Closure: una función recuerda el entorno donde se creó.

**Micro-ejemplo**

```js
function counter(){ let x=0; return ()=> ++x; }
const c = counter(); console.log(c(), c()); // 1 2
```

---

## 09. Errores

**Qué entender**

* Manejo con `try/catch/finally`.
* Crea errores propios para mensajes claros.

**Micro-ejemplo**

```js
try { throw new Error("Oops"); } catch (e) { console.error(e.message); }
```

---

## 10. Asincronía

**Qué entender**

* Promesas modelan trabajo futuro; `async/await` simplifica el flujo.
* Usa `try/catch` en funciones `async`.

**Micro-ejemplo**

```js
const delay = ms => new Promise(r => setTimeout(r, ms));
(async ()=>{ await delay(200); console.log("Listo"); })();
```

---

## Buenas prácticas rápidas

* **`const` > `let` > `var`**.
* Igualdad estricta `===`.
* Nombra funciones/variables con intención.
* Maneja errores (no ignores rechazos de promesas).
* Pequeños scripts, responsabilidades claras.

---

## Glosario mínimo

* **Coerción**: conversión implícita de tipos (p. ej., `"2"*3` → `6`).
* **Truthy/Falsy**: valores que se tratan como `true`/`false` en condiciones.
* **Closure**: función que “recuerda” variables del entorno donde se creó.
* **ESM**: sistema de módulos estándar (`export`/`import`).
* **Hoisting**: comportamiento de “elevación” de declaraciones al inicio del ámbito.

---

## ✍️ Créditos

Desarrollado con fines educativos with ❤️ by [@luuiscc_](https://github.com/luuuisc) 
