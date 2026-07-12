"""
statistics.py
-------------

Módulo de análisis estadístico del corpus.
"""

from collections import Counter


def obtener_palabras(texto):

    palabras = []

    for linea in texto.splitlines():

        linea = linea.strip()

        if not linea:
            continue

        # Ignorar comentarios
        if linea.startswith("#"):
            continue

        # Ignorar etiquetas entre <>
        if linea.startswith("<"):
            continue

        palabras.extend(linea.split())

    return palabras


def frecuencia_palabras(palabras):
    return Counter(palabras)


def frecuencia_simbolos(palabras):

    contador = Counter()

    for palabra in palabras:

        contador.update(palabra)

    return contador


def longitud_media(palabras):

    if not palabras:
        return 0

    return sum(len(p) for p in palabras) / len(palabras)


def palabras_unicas(palabras):

    return len(set(palabras))
