"""Estrategia 1: lista ordenada por ID.

Buscar:   O(log N) con busqueda binaria (modulo bisect de la libreria estandar).
Insertar: O(N) porque hay que correr elementos para mantener el orden.
"""

import bisect


class ListaEstudiantes:

    def __init__(self):
        self.ids = []          # IDs ordenados de menor a mayor
        self.estudiantes = []  # estudiantes en el mismo orden que los IDs

    def insertar(self, estudiante):
        # bisect encuentra la posicion correcta; insert corre los elementos
        pos = bisect.bisect_left(self.ids, estudiante.id)
        self.ids.insert(pos, estudiante.id)
        self.estudiantes.insert(pos, estudiante)

    def buscar(self, id_):
        pos = bisect.bisect_left(self.ids, id_)
        if pos < len(self.ids) and self.ids[pos] == id_:
            return self.estudiantes[pos]
        return None

    def listar(self):
        # ya estan ordenados por ID
        return list(self.estudiantes)
