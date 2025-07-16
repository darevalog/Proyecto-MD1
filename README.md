# 🧠 Parser de Fórmulas Bien Formadas (FBF) en LaTeX

Este proyecto en Python permite tomar una fórmula lógica escrita en notación LaTeX y transformarla en su versión estructurada como **Fórmula Bien Formada** (FBF). Es útil para estudiantes de lógica matemática que deseen validar la sintaxis estructural de proposiciones complejas.

---

## 📌 Características

- Interpreta entrada LaTeX en consola, delimitada por signos `$...$`.
- Reconoce conectores lógicos: `\neg`, `\land`, `\lor`, `\rightarrow`, `\leftrightarrow`.
- Agrupa automáticamente con paréntesis según la jerarquía lógica.
- Devuelve una versión bien formada, útil para análisis y demostraciones.

---

## 🧩 Estructura del código

### `separar()`

- Solicita una entrada en consola: debe estar delimitada por signos `$...$`.
- Filtra los espacios y separa la fórmula en una lista de tokens.
- Identifica los operadores lógicos en LaTeX y los normaliza.
- Retorna la fórmula en forma de lista de símbolos.

---

### `devolver(d: list)`

- Recibe una fórmula como lista de cadenas.
- Devuelve la expresión con formato LaTeX, incluyendo los delimitadores `$...$`.

---

### `devolverS(d: list)`

- Une los elementos de la lista en un solo string, separados por espacio, sin los signos `$`.

---

### `parentesis(formula: list)`

- Busca subfórmulas encerradas entre paréntesis.
- Llama recursivamente a `FBF` sobre ellas para asegurar que cada parte esté bien formada.
- Reemplaza subexpresiones en la lista principal.

---

### `negacion(formula: list)`

- Detecta el operador `\neg`.
- Agrupa el operando inmediatamente posterior dentro de paréntesis.
- Modifica la lista para que esta negación sea tratada como una subfórmula completa.

---

### `o_y_Logico(formula: list)`

- Identifica los conectores `\lor` (disyunción) y `\land` (conjunción).
- Agrupa los operandos izquierdo y derecho, y los encierra en paréntesis.

---

### `implicacion_equivalencia(formula: list)`

- Procesa conectores `\rightarrow` (implicación) y `\leftrightarrow` (bicondicional).
- Agrupa ambos lados de la relación con paréntesis.

---

### `FBF(formula: list)`

Función principal que garantiza que una fórmula está bien formada siguiendo esta jerarquía de operadores:

1. Paréntesis
2. Negación
3. Disyunción / Conjunción
4. Implicación / Equivalencia

Devuelve la fórmula como lista, lista para ser convertida nuevamente a LaTeX.

---

### 🧪 Ejemplo de uso

```bash
$ python main.py
$ \neg p \rightarrow ( q \land r ) $
$ (\neg p) \rightarrow (q \land r) $
