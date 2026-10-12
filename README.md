# Laboratorio 3: Sistema de Búsqueda

Sistema para administrar estudiantes (ID, nombre, edad, promedio) con tres
estrategias de almacenamiento y búsqueda: **lista ordenada**, **árbol binario
de búsqueda (ABB)** y **árbol B+**.

El objetivo del laboratorio es **medir experimentalmente** cómo escala el tiempo
de búsqueda e inserción al crecer el tamaño N de los datos, comparando las tres
estrategias, con datos insertados en orden aleatorio y en orden creciente.

## Requisitos

- Python 3.10+
- matplotlib: `pip install matplotlib`

(No se usa numpy ni pandas: basta la librería estándar.)

## Menú manual

```bash
cd src
python main.py
```

## Experimentos

```bash
cd src
python experimento.py   # mide tiempos -> datos/tiempos.csv y datos/resumen.csv
python graficas.py      # genera resultados/busqueda.png, insercion.png, altura.png
```

Parámetros (en `src/experimento.py`):

- `N_VALORES`: tamaños de entrada N
- `FACTOR_BUSQUEDAS`: M = fracción de N (cantidad de búsquedas aleatorias)
- `REPETICIONES`: R, repeticiones por caso
- `SEMILLA`: semilla fija para reproducibilidad

Nota: el ABB no está balanceado; con datos ordenados degenera a O(N), por lo
que tamaños grandes (20000+) tardan bastante. Agrégalos con paciencia.

## Estructura

```
src/
  main.py            menú de consola (insertar / buscar / listar)
  estudiante.py      dataclass Estudiante
  estructuras/
    lista.py         lista ordenada (búsqueda binaria con bisect)
    abb.py           árbol binario de búsqueda (sin balanceo)
    bmas.py          árbol B+ (orden 4, hojas enlazadas)
  experimento.py     genera datos, mide tiempos, calcula estadísticas
  graficas.py        dibuja las gráficas (PNG)
datos/               CSV con los tiempos (crudos y resumen)
resultados/          gráficas PNG
```

## Para el informe

Registra: hardware, versión de Python, N, M, R, semilla, cómo se generaron los
datos y las búsquedas, método de medición (`time.perf_counter`), tratamiento de
valores atípicos y estadísticas (promedio, desviación estándar).
