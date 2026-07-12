"""
reports.py
-----------

Generación de informes para VIM-1
"""

from pathlib import Path


def guardar_reporte(
    total_palabras,
    palabras_unicas,
    longitud_media,
    top_palabras,
    top_simbolos,
):

    carpeta = Path("analysis")
    carpeta.mkdir(exist_ok=True)

    archivo = carpeta / "report.txt"

    with archivo.open("w", encoding="utf-8") as f:

        f.write("PROYECTO ALETHEIA–VOYNICH\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Total de palabras: {total_palabras}\n")
        f.write(f"Palabras únicas: {palabras_unicas}\n")
        f.write(f"Longitud media: {longitud_media:.2f}\n\n")

        f.write("20 palabras más frecuentes\n")
        f.write("--------------------------\n")

        for palabra, frecuencia in top_palabras:
            f.write(f"{palabra:20} {frecuencia}\n")

        f.write("\n20 símbolos más frecuentes\n")
        f.write("--------------------------\n")

        for simbolo, frecuencia in top_simbolos:
            f.write(f"{simbolo:5} {frecuencia}\n")

    print("\n✅ Informe generado correctamente.")
