"""Experimento: mide el tiempo de insercion y busqueda de las 3 estructuras.

Uso:
    cd src
    python experimento.py

Genera:
    ../datos/tiempos.csv   tiempos crudos (una fila por repeticion)
    ../datos/resumen.csv   promedio y desviacion estandar por caso
"""

import csv
import os
import random
import statistics
import time

from estudiante import Estudiante
from estructuras.abb import ABB
from estructuras.bmas import BPlus
from estructuras.lista import ListaEstudiantes

# ---------- parametros del experimento (ajustar aqui) ----------
N_VALORES = [100, 1000, 5000, 10000]   # tamaños de entrada N
FACTOR_BUSQUEDAS = 0.1   # M = 10% de N (cantidad de busquedas aleatorias)
REPETICIONES = 5         # R: veces que se repite cada caso
SEMILLA = 42             # semilla fija = resultados reproducibles

ESTRUCTURAS = {           # nombre -> clase
    "lista": ListaEstudiantes,
    "abb": ABB,
    "bmas": BPlus,
}

CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "..", "datos")
RUTA_CRUDOS = os.path.join(CARPETA_DATOS, "tiempos.csv")
RUTA_RESUMEN = os.path.join(CARPETA_DATOS, "resumen.csv")


def generar_estudiantes(n, ordenado=False, semilla=SEMILLA):
    """Crea n estudiantes con IDs de 1 a n, al azar o en orden creciente."""
    rng = random.Random(semilla + n)
    ids = list(range(1, n + 1))
    if not ordenado:
        rng.shuffle(ids)                    # IDs distribuidos al azar
    return [
        Estudiante(id_, f"Estudiante {id_}", rng.randint(17, 25),
                   round(rng.uniform(0.0, 5.0), 2))
        for id_ in ids
    ]


def medir_insercion(fabrica, estudiantes):
    """Inserta todos los estudiantes y devuelve (estructura, tiempo en segundos)."""
    estructura = fabrica()
    inicio = time.perf_counter()            # reloj de alta resolucion
    for estudiante in estudiantes:
        estructura.insertar(estudiante)
    return estructura, time.perf_counter() - inicio


def medir_busqueda(estructura, ids_busqueda):
    """Realiza M busquedas y devuelve el tiempo total en segundos."""
    inicio = time.perf_counter()
    for id_ in ids_busqueda:
        estructura.buscar(id_)
    return time.perf_counter() - inicio


def ejecutar():
    random.seed(SEMILLA)
    os.makedirs(CARPETA_DATOS, exist_ok=True)
    filas = []

    for n in N_VALORES:
        m = max(1, int(n * FACTOR_BUSQUEDAS))
        for tipo in ("aleatorio", "ordenado"):
            estudiantes = generar_estudiantes(n, ordenado=(tipo == "ordenado"))
            # los IDs de busqueda son M IDs existentes, elegidos al azar
            ids_busqueda = random.sample(range(1, n + 1), m)

            for nombre, fabrica in ESTRUCTURAS.items():
                for repeticion in range(1, REPETICIONES + 1):
                    estructura, t_insercion = medir_insercion(fabrica, estudiantes)
                    t_busqueda = medir_busqueda(estructura, ids_busqueda)
                    altura = estructura.altura() if hasattr(estructura, "altura") else ""
                    filas.append({
                        "estrategia": nombre,
                        "tipo_datos": tipo,
                        "n": n,
                        "m": m,
                        "repeticion": repeticion,
                        "tiempo_insercion_s": round(t_insercion, 6),
                        "tiempo_busqueda_s": round(t_busqueda, 6),
                        "altura": altura,
                    })
                    print(f"N={n:>6} | {tipo:<9} | {nombre:<6} | rep {repeticion} | "
                          f"insercion {t_insercion:8.4f} s | busqueda {t_busqueda:.6f} s")

    with open(RUTA_CRUDOS, "w", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        escritor.writeheader()
        escritor.writerows(filas)

    resumir(filas)
    print(f"\nListo: {RUTA_CRUDOS} y {RUTA_RESUMEN}")


def resumir(filas):
    """Agrupa por (estrategia, tipo, N) y calcula promedio y desviacion estandar."""
    grupos = {}
    for fila in filas:
        clave = (fila["estrategia"], fila["tipo_datos"], fila["n"])
        grupos.setdefault(clave, []).append(fila)

    resumen = []
    for (estrategia, tipo, n), grupo in sorted(grupos.items()):
        inserciones = [f["tiempo_insercion_s"] for f in grupo]
        busquedas = [f["tiempo_busqueda_s"] for f in grupo]
        alturas = [f["altura"] for f in grupo if f["altura"] != ""]
        resumen.append({
            "estrategia": estrategia,
            "tipo_datos": tipo,
            "n": n,
            "m": grupo[0]["m"],
            "repeticiones": len(grupo),
            "insercion_promedio_s": statistics.mean(inserciones),
            "insercion_stdev_s": statistics.stdev(inserciones) if len(grupo) > 1 else 0.0,
            "busqueda_promedio_s": statistics.mean(busquedas),
            "busqueda_stdev_s": statistics.stdev(busquedas) if len(grupo) > 1 else 0.0,
            "altura_promedio": statistics.mean(alturas) if alturas else "",
        })

    with open(RUTA_RESUMEN, "w", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=list(resumen[0].keys()))
        escritor.writeheader()
        escritor.writerows(resumen)


if __name__ == "__main__":
    ejecutar()
