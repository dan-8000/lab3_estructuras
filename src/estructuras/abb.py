"""Estrategia 2: arbol binario de busqueda (ABB), sin balanceo.

Buscar/insertar: O(log N) en promedio con IDs aleatorios, pero O(N) si los
IDs se insertan ordenados (el arbol se degenera en una lista).
Las inserciones son iterativas porque un arbol degenerado de muchos nodos
reventaria el limite de recursion de Python.
"""


class NodoABB:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.izquierda = None   # IDs menores
        self.derecha = None     # IDs mayores


class ABB:

    def __init__(self):
        self.raiz = None

    def insertar(self, estudiante):
        if self.raiz is None:
            self.raiz = NodoABB(estudiante)
            return
        nodo = self.raiz
        while True:
            if estudiante.id < nodo.estudiante.id:
                if nodo.izquierda is None:
                    nodo.izquierda = NodoABB(estudiante)
                    return
                nodo = nodo.izquierda
            else:
                if nodo.derecha is None:
                    nodo.derecha = NodoABB(estudiante)
                    return
                nodo = nodo.derecha

    def buscar(self, id_):
        nodo = self.raiz
        while nodo is not None:
            if id_ == nodo.estudiante.id:
                return nodo.estudiante
            nodo = nodo.izquierda if id_ < nodo.estudiante.id else nodo.derecha
        return None

    def listar(self):
        # recorrido in-orden con pila explicita: devuelve los ID en orden ascendente
        resultado = []
        pila = []
        nodo = self.raiz
        while pila or nodo is not None:
            while nodo is not None:
                pila.append(nodo)
                nodo = nodo.izquierda
            nodo = pila.pop()
            resultado.append(nodo.estudiante)
            nodo = nodo.derecha
        return resultado

    def altura(self):
        """Altura en niveles (raiz = 1). Sirve para correlacionar con el tiempo de busqueda."""
        if self.raiz is None:
            return 0
        altura = 0
        nivel = [self.raiz]
        while nivel:
            altura += 1
            siguiente = []
            for nodo in nivel:
                if nodo.izquierda:
                    siguiente.append(nodo.izquierda)
                if nodo.derecha:
                    siguiente.append(nodo.derecha)
            nivel = siguiente
        return altura
