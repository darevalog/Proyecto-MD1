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

Esta función solicita una entrada del usuario (por consola), que debe estar delimitada por signos de dólar (`$...$`). Luego:

1. Elimina los espacios y filtra los caracteres relevantes.
2. Reconoce operadores como `\neg`, `\lor`, `\land`, `\rightarrow` y `\leftrightarrow` caracter por caracter, convirtiéndolos en una sola cadena.
3. Verifica que los delimitadores `$` están correctamente ubicados.
4. Devuelve la fórmula como una lista de símbolos procesados (tokens).

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
Recibe una fórmula estructurada (una lista de símbolos o subfórmulas) y la convierte nuevamente a formato LaTeX como cadena, añadiendo los signos $ al inicio y final. Esto permite imprimir el resultado de manera legible como si fuera una fórmula en un documento.

```python
def devolver(d:list):
   a=""
   for i in d:
      a=a+i+" "
   return ("$"+a+"$")
```
---

### `devolverS(d: list)`

Esta función toma una lista de elementos (por ejemplo, una subfórmula como ["p", "\land", "q"]) y los convierte en una sola cadena unida por espacios, como "p \land q". Es usada para construir subfórmulas agrupadas.

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
Se encarga de detectar subexpresiones entre paréntesis y procesarlas de forma recursiva con la función FBF. Esto asegura que las expresiones internas también estén bien formadas antes de integrarse a la fórmula general. Usa una pila implícita (contador) para detectar el cierre de cada paréntesis.

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
Revisa la fórmula buscando el operador \neg. Cuando lo encuentra, agrupa este operador con su operando (ya sea una variable o una subfórmula entre paréntesis). De este modo, la negación se interpreta correctamente como un solo bloque lógico.

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

Identifica los conectores binarios \lor y \land, y agrupa el operando izquierdo y derecho con el operador dentro de un paréntesis. Esto garantiza que operaciones conjuntas se consideren como una sola subfórmula.

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

Procesa los operadores \rightarrow y \leftrightarrow, agrupando el operando izquierdo y derecho junto con el operador. Esto asegura que la implicación y equivalencia se entiendan como bloques bien definidos.

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

> :shipit: Diego Alejandro Arévalo Guevara. July 17, 2025.
