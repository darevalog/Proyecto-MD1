# 🧠 Parser de Fórmulas Bien Formadas (FBF) en LaTeX

Este proyecto en Python transforma expresiones lógicas escritas en LaTeX en una **Fórmula Bien Formada (FBF)** estructurada. Ideal para estudiantes de lógica que deseen verificar o manipular fórmulas simbólicas.

---

## 📌 Características

- Interpreta expresiones delimitadas con `$...$`.
- Reconoce conectores lógicos: `\neg`, `\land`, `\lor`, `\rightarrow`, `\leftrightarrow`.
- Agrupa con paréntesis según la jerarquía lógica.
- Devuelve la fórmula reestructurada en formato LaTeX.

---

## 🧩 Explicación del código

### `separar()`

Esta función:
- Recibe la entrada del usuario.
- Elimina espacios innecesarios.
- Detecta operadores LaTeX como `\neg`, `\land`, etc.
- Retorna la fórmula como lista de símbolos.

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
