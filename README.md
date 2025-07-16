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

```python
def separar():
    b=input()
    s=[]
    n=[]
    for i in b:
        if i==" " or i=="$":
            if i=="$":
               n.append(len(s))
            pass
        else:
            s.append(i)
    if len(n)!=2 or n[0]!=0 or n[1]!=len(s):
       return (f"Esto no es una entrada latex:")
    s1=[]
    veri=0
    for i in range(len(s)):
        if s[i]== "\\":
            if (s[i+1]+s[i+2]+s[i+3])=="neg":
              s1.append("\\neg")
              veri=i+3
            elif (s[i+1]+s[i+2]+s[i+3])=="lor":
              s1.append("\\lor")
              veri=i+3
            elif (s[i+1]+s[i+2]+s[i+3]+s[i+4])=="land":
              s1.append("\\land")
              veri=i+4
            elif (s[i+1:i+11])=="rightarrow":
              s1.append("\\rightarrow")
              veri=i+10
            elif (s[i+1:i+15])=="leftrightarrow":
              s1.append("\\leftrightarrow")
              veri=i+14
        else:
            if(veri<i or veri==0):
                s1.append(s[i])
    return s1
```
---

### `devolver(d: list)`

- Recibe una fórmula como lista de cadenas.
- Devuelve la expresión con formato LaTeX, incluyendo los delimitadores `$...$`.

```python
def devolver(d:list):
   a=""
   for i in d:
      a=a+i+" "
   return ("$"+a+"$")
```
---

### `devolverS(d: list)`

- Une los elementos de la lista en un solo string, separados por espacio, sin los signos `$`.

```python
def devolverS(d:list):
   a=""
   for i in range(len(d)):
     if i==len(d)-1:
       a=a+d[i]
     else:
      a=a+d[i]+" "
   return (a)

```
---

### `parentesis(formula: list)`

- Busca subfórmulas encerradas entre paréntesis.
- Llama recursivamente a `FBF` sobre ellas para asegurar que cada parte esté bien formada.
- Reemplaza subexpresiones en la lista principal.

```python
def parentesis(formula:list):
  termino = []
  i = 0
  contador = 0
  w = False
  while i < len(formula):
    if contador > 0:
      w = True
    if formula[i] == '(':
      contador = contador + 1
    if formula[i] == ')':
      contador = contador - 1
      if contador == 0:
        formula.insert(i, devolverS(FBF(termino)))
        termino.clear()
        formula.pop(i + 1)
        formula.pop(i - 1)
        i = i
        w = False
    if contador > 0 and w:
      termino.append(formula[i])
      formula.pop(i)
      i = i - 1
    i = i + 1
  return formula

```

---

### `negacion(formula: list)`

- Detecta el operador `\neg`.
- Agrupa el operando inmediatamente posterior dentro de paréntesis.
- Modifica la lista para que esta negación sea tratada como una subfórmula completa.

```python
def negacion(formula:list):
  termino = []
  Largo = len(formula) - 1
  for i in range(Largo + 1):
    if formula[Largo - i] == "\\neg" and formula[Largo - i + 1][0] != "(":
      termino.append(formula[Largo - i])
      termino.append('(')
      termino.append(formula[Largo - i + 1])
      termino.append(')')
      formula.pop(Largo - i + 1)
      formula.pop(Largo - i)
      formula.insert(Largo - i, devolverS(termino))
      termino.clear()
    elif formula[Largo - i] == "\\neg" and formula[Largo - i + 1][0] == "(":
      termino.append(formula[Largo - i])
      termino.append(formula[Largo - i + 1])
      formula.pop(Largo - i + 1)
      formula.pop(Largo - i)
      formula.insert(Largo - i, devolverS(termino))
      termino.clear()
  return formula

```
---

### `o_y_Logico(formula: list)`

- Identifica los conectores `\lor` (disyunción) y `\land` (conjunción).
- Agrupa los operandos izquierdo y derecho, y los encierra en paréntesis.

```python
def o_y_Logico(formula:list):
  termino = []
  i = 0
  while i < len(formula):
    if formula[i] == "\\lor" or formula[i] == "\\land":
      termino.append('(')
      termino.append(formula[i-1])
      termino.append(formula[i])
      termino.append(formula[i+1])
      termino.append(')')
      formula.pop(i+1)
      formula.pop(i)
      formula.pop(i-1)
      formula.insert(i-1, devolverS(termino))
      i = i - 1
      termino.clear()
    i = i + 1
  return formula

```

---

### `implicacion_equivalencia(formula: list)`

- Procesa conectores `\rightarrow` (implicación) y `\leftrightarrow` (bicondicional).
- Agrupa ambos lados de la relación con paréntesis.

```python
def implicacion_equivalencia(formula:list):
  termino = []
  i = 0
  while i < len(formula):
    if formula[i] == "\\leftrightarrow" or formula[i] == "\\rightarrow":
      termino.append('(')
      termino.append(formula[i-1])
      termino.append(formula[i])
      termino.append(formula[i+1])
      termino.append(')')
      formula.pop(i+1)
      formula.pop(i)
      formula.pop(i-1)
      formula.insert(i-1, devolverS(termino))
      i = i - 1
      termino.clear()
    i = i + 1
  return formula

```
---

### `FBF(formula: list)`

Función principal que garantiza que una fórmula está bien formada siguiendo esta jerarquía de operadores:

1. Paréntesis
2. Negación
3. Disyunción / Conjunción
4. Implicación / Equivalencia

Devuelve la fórmula como lista, lista para ser convertida nuevamente a LaTeX.

```python
def FBF(formula:list):
  formula = parentesis(formula)
  formula = negacion(formula)
  formula = o_y_Logico(formula)
  formula = implicacion_equivalencia(formula)
  return(formula)

```
---

### 🧪 Ejemplo de uso

```bash
$ python main.py
$ \neg p \rightarrow ( q \land r ) $
$ (\neg p) \rightarrow (q \land r) $
```
