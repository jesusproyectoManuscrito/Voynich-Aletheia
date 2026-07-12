"""
Proyecto Aletheia–Voynich
VIM-1 Corpus Analyzer
Versión 0.3
"""

from pathlib import Path
from collections import Counter

CORPUS = Path("ZL3a-n.txt")

print("=" * 60)
print("VIM-1 Corpus Analyzer v0.3")
print("=" * 60)

if not CORPUS.exists():
    print("ERROR: No se encontró ZL3a-n.txt")
    exit()

texto = CORPUS.read_text(encoding="utf-8")

palabras = []

for linea in texto.splitlines():

    linea = linea.strip()

    if not linea:
        continue

    if linea.startswith("#"):
        continue

    for palabra in linea.split():
        palabras.append(palabra)

contador = Counter(palabras)

print(f"\nTotal de palabras: {len(palabras)}")
print(f"Palabras distintas: {len(contador)}")

print("\nLas 20 palabras más frecuentes:\n")

for palabra, frecuencia in contador.most_common(20):
    print(f"{palabra:20} {frecuencia}")
# Guardar informe

from pathlib import Path

salida = Path("analysis/report.txt")

with salida.open("w", encoding="utf-8") as f:

    f.write("PROYECTO ALETHEIA-VOYNICH\n")
    f.write("=========================\n\n")

    f.write(f"Total de palabras: {len(palabras)}\n")
    f.write(f"Palabras distintas: {len(contador)}\n\n")

    f.write("20 palabras más frecuentes\n")
    f.write("--------------------------\n")

    for palabra, frecuencia in contador.most_common(20):
        f.write(f"{palabra:20} {frecuencia}\n")

print("\nInforme guardado correctamente.")
