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
              pass
            elif (s[i+1]+s[i+2]+s[i+3])=="lor":
              s1.append("\lor")
              veri=i+3
              pass
            elif (s[i+1]+s[i+2]+s[i+3]+s[i+4])=="land":
              s1.append("\land")
              veri=i+4
              pass
            elif (s[i+1]+s[i+2]+s[i+3]+s[i+4]+s[i+5]+s[i+6]+s[i+7]+s[i+8]+s[i+9]+s[i+10])=="rightarrow":
              s1.append("\\rightarrow")
              veri=i+10
              pass
            elif (s[i+1]+s[i+2]+s[i+3]+s[i+4]+s[i+5]+s[i+6]+s[i+7]+s[i+8]+s[i+9]+s[i+10]+s[i+11]+s[i+12]+s[i+13]+s[i+14])=="leftrightarrow":
              s1.append("\leftrightarrow")
              veri=i+14
              pass
        else:
            if(veri<i or veri==0):
                s1.append(s[i])
    #print (s)
    return s1


def devolver(d:list):
   return ("$"+d[0]+"$")

def devolverS(d:list):
   a=""
   for i in range(len(d)):
     if i==len(d)-1:
       a=a+d[i]
     else:
      a=a+d[i]+" "
   return (a)

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

def FBF(formula:list):
  formula = parentesis(formula)
  formula = negacion(formula)
  formula = o_y_Logico(formula)
  formula = implicacion_equivalencia(formula)

  return(formula)

FormulaBienFormada = FBF(separar())
print(devolver(FormulaBienFormada))
