# 🧠 Proyecto de Matemáticas Discretas - Parseador de Lógica en LaTeX

Este repositorio contiene un pequeño sistema que permite leer expresiones de lógica proposicional escritas en formato LaTeX, separarlas en componentes y reconstruirlas. Está orientado a estudiantes de matemáticas discretas o lógica computacional.

## ✨ Características

- Interpreta expresiones lógicas escritas como `$\neg p \lor q$`
- Separa conectivos lógicos: ¬, ∨, ∧, →, ↔
- Permite devolver la expresión en formato reconstruido

## 📂 Estructura

- `main.py` — Punto de entrada para probar el programa
- `utils/latex_parser.py` — Funciones para analizar y recomponer expresiones
- `README.md` — Esta documentación

## ▶️ Ejecución

```bash
python main.py
