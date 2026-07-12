"""
reader.py
----------

Se encarga de cargar el corpus del Manuscrito Voynich.
"""

from pathlib import Path


RUTAS_CORPUS = [
    Path("corpus/ZL3a-n.txt"),
    Path("ZL3a-n.txt")
]


def cargar_corpus():

    for ruta in RUTAS_CORPUS:

        if ruta.exists():

            print(f"Corpus encontrado: {ruta}")

            return ruta.read_text(
                encoding="utf-8"
            )

    raise FileNotFoundError(
        "No se encontró el archivo ZL3a-n.txt"
    )
