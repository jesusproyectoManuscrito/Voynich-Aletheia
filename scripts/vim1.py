"""
Proyecto Aletheia–Voynich
VIM-1 Corpus Analyzer
Versión 0.5
"""

from pathlib import Path
from collections import Counter

CORPUS = Path("corpus/ZL3a-n.txt")

if not CORPUS.exists():
    CORPUS = Path("ZL3a-n.txt")

texto = CORPUS.read_text(encoding="utf-8")

palabras = []

for linea in texto.splitlines():

    linea = linea.strip()

    if not linea:
        continue

    if linea.startswith("#"):
        continue

    palabras.extend(linea.split())

contador_palabras = Counter(palabras)

contador_simbolos = Counter()

for palabra in palabras:
    for simbolo in palabra:
        contador_simbolos[simbolo] += 1

print("=" * 60)
print("VIM-1 Corpus Analyzer v0.5")
print("=" * 60)

print(f"Palabras totales : {len(palabras)}")
print(f"Palabras únicas  : {len(contador_palabras)}")
print(f"Símbolos únicos  : {len(contador_simbolos)}")

print("\n20 palabras más frecuentes")
for palabra, frecuencia in contador_palabras.most_common(20):
    print(f"{palabra:20} {frecuencia}")

print("\n20 símbolos más frecuentes")
for simbolo, frecuencia in contador_simbolos.most_common(20):
    print(f"{simbolo:3} {frecuencia}")
