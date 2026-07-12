"""
Proyecto Aletheia–Voynich
VIM-1 Corpus Analyzer
Versión 0.2
"""

from pathlib import Path

CORPUS = Path("ZL3a-n.txt")

print("=" * 50)
print("VIM-1 Corpus Analyzer")
print("=" * 50)

if not CORPUS.exists():
    print("ERROR: No se encontró el archivo ZL3a-n.txt")
    exit()

texto = CORPUS.read_text(encoding="utf-8")

lineas = texto.splitlines()

palabras = []

for linea in lineas:

    linea = linea.strip()

    if linea == "":
        continue

    if linea.startswith("#"):
        continue

    partes = linea.split()

    for palabra in partes:
        palabras.append(palabra)

print(f"Total de líneas : {len(lineas)}")
print(f"Total de palabras : {len(palabras)}")
print(f"Primeras 20 palabras:")

for palabra in palabras[:20]:
    print(" -", palabra)
