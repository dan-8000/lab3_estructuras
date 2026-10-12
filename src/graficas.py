"""Genera las graficas del experimento a partir de datos/resumen.csv.

Uso:
    cd src
    python graficas.py

Guarda en ../resultados/: busqueda.png, insercion.png, altura.png
"""

import csv
import os

import matplotlib
matplotlib.use("Agg")            # modo sin ventana (solo guardar PNG)
import matplotlib.pyplot as plt

CARPETA = os.path.dirname(__file__)
RUTA_RESUMEN = os.path.join(CARPETA, "..", "datos", "resumen.csv")
CARPETA_RESULTADOS = os.path.join(CARPETA, "..", "resultados")

# marcador y nombre visible de cada estrategia
ESTILOS = {
    "lista": ("o", "Lista ordenada"),
    "abb": ("s", "ABB"),
    "bmas": ("^", "B+"),
}


def cargar_resumen():
    with open(RUTA_RESUMEN) as f:
        return list(csv.DictReader(f))


def _puntos(filas, estrategia, tipo, columna):
    return sorted(
        (int(f["n"]), float(f[columna]))
        for f in filas
        if f["estrategia"] == estrategia and f["tipo_datos"] == tipo
    )


def graficar_tiempos(filas, columna, archivo, titulo):
    fig, ax = plt.subplots(figsize=(8, 5))
    for estrategia, (marcador, nombre) in ESTILOS.items():
        for tipo in ("aleatorio", "ordenado"):
            puntos = _puntos(filas, estrategia, tipo, columna)
            if not puntos:
                continue
            x, y = zip(*puntos)
            ax.plot(x, y, marker=marcador,
                    linestyle="--" if tipo == "ordenado" else "-",
                    label=f"{nombre} ({tipo})")
    ax.set_xscale("log")               # eje X logaritmico: abarca de 100 a 50000
    ax.set_yscale("log")               # eje Y logaritmico: se ven todas las curvas
    ax.set_title(titulo)
    ax.set_xlabel("N (cantidad de estudiantes)")
    ax.set_ylabel("Tiempo (segundos)")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(CARPETA_RESULTADOS, archivo))
    plt.close(fig)


def graficar_altura(filas):
    """Altura de los arboles vs N: explica por que cambia el tiempo de busqueda."""
    fig, ax = plt.subplots(figsize=(8, 5))
    for estrategia in ("abb", "bmas"):
        marcador, nombre = ESTILOS[estrategia]
        for tipo in ("aleatorio", "ordenado"):
            puntos = _puntos(filas, estrategia, tipo, "altura_promedio")
            if not puntos:
                continue
            x, y = zip(*puntos)
            ax.plot(x, y, marker=marcador,
                    linestyle="--" if tipo == "ordenado" else "-",
                    label=f"{nombre} ({tipo})")
    ax.set_xscale("log")
    ax.set_title("Altura del arbol vs tamaño de datos")
    ax.set_xlabel("N (cantidad de estudiantes)")
    ax.set_ylabel("Altura (niveles)")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(CARPETA_RESULTADOS, "altura.png"))
    plt.close(fig)


def main():
    os.makedirs(CARPETA_RESULTADOS, exist_ok=True)
    filas = cargar_resumen()
    graficar_tiempos(filas, "busqueda_promedio_s", "busqueda.png",
                     "Tiempo de busqueda vs tamaño de datos")
    graficar_tiempos(filas, "insercion_promedio_s", "insercion.png",
                     "Tiempo de insercion vs tamaño de datos")
    graficar_altura(filas)
    print("Graficas guardadas en resultados/")


if __name__ == "__main__":
    main()
