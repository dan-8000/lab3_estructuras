"""Estrategia 3: arbol B+ de orden pequeno (por defecto 4).

Buscar/insertar: O(log N) siempre, porque el arbol se balancea solo al dividir
nodos. Las hojas estan enlazadas, asi que listar es un recorrido lineal.
Nota: en un B+ real el orden seria mucho mayor; aqui es pequeno para que el
codigo sea simple y entendible.
"""


class NodoBPlus:
    def __init__(self, hoja=False):
        self.claves = []        # IDs
        self.estudiantes = []   # solo en hojas
        self.hijos = []         # solo en nodos internos
        self.hoja = hoja
        self.siguiente = None   # enlace a la siguiente hoja (para listar en orden)


class BPlus:

    def __init__(self, orden=4):
        # cada nodo guarda como maximo 'orden' claves
        self.orden = orden
        self.raiz = NodoBPlus(hoja=True)

    # ---------- operaciones publicas ----------

    def insertar(self, estudiante):
        resultado = self._insertar(self.raiz, estudiante)
        if resultado is not None:
            # la raiz se dividio: crear una nueva raiz con la clave promovida
            clave, nuevo = resultado
            raiz = NodoBPlus()
            raiz.claves = [clave]
            raiz.hijos = [self.raiz, nuevo]
            self.raiz = raiz

    def buscar(self, id_):
        nodo = self.raiz
        while not nodo.hoja:
            nodo = nodo.hijos[self._indice_hijo(nodo, id_)]
        # la hoja tiene pocas claves (<= orden), basta con un recorrido lineal
        for i, clave in enumerate(nodo.claves):
            if clave == id_:
                return nodo.estudiantes[i]
        return None

    def listar(self):
        # ir a la primera hoja y recorrer el enlace de hojas
        nodo = self.raiz
        while not nodo.hoja:
            nodo = nodo.hijos[0]
        resultado = []
        while nodo is not None:
            resultado.extend(nodo.estudiantes)
            nodo = nodo.siguiente
        return resultado

    def altura(self):
        altura = 1
        nodo = self.raiz
        while not nodo.hoja:
            altura += 1
            nodo = nodo.hijos[0]
        return altura

    # ---------- insercion recursiva ----------
    # devuelve (clave_promovida, nuevo_nodo) si el nodo se dividio, sino None

    def _insertar(self, nodo, estudiante):
        if nodo.hoja:
            self._insertar_en_hoja(nodo, estudiante)
            if len(nodo.claves) > self.orden:
                return self._dividir_hoja(nodo)
            return None
        # nodo interno: bajar al hijo que corresponde
        i = self._indice_hijo(nodo, estudiante.id)
        resultado = self._insertar(nodo.hijos[i], estudiante)
        if resultado is None:
            return None
        clave, nuevo = resultado
        nodo.claves.insert(i, clave)
        nodo.hijos.insert(i + 1, nuevo)
        if len(nodo.claves) > self.orden:
            return self._dividir_interno(nodo)
        return None

    def _indice_hijo(self, nodo, id_):
        # primer hijo cuya clave separadora es mayor que id_
        i = 0
        while i < len(nodo.claves) and id_ >= nodo.claves[i]:
            i += 1
        return i

    def _insertar_en_hoja(self, hoja, estudiante):
        i = 0
        while i < len(hoja.claves) and hoja.claves[i] < estudiante.id:
            i += 1
        hoja.claves.insert(i, estudiante.id)
        hoja.estudiantes.insert(i, estudiante)

    def _dividir_hoja(self, hoja):
        medio = len(hoja.claves) // 2
        nueva = NodoBPlus(hoja=True)
        nueva.claves = hoja.claves[medio:]
        nueva.estudiantes = hoja.estudiantes[medio:]
        hoja.claves = hoja.claves[:medio]
        hoja.estudiantes = hoja.estudiantes[:medio]
        nueva.siguiente = hoja.siguiente
        hoja.siguiente = nueva
        return nueva.claves[0], nueva     # se promociona el primer ID de la hoja nueva

    def _dividir_interno(self, nodo):
        medio = len(nodo.claves) // 2
        nueva = NodoBPlus()
        nueva.claves = nodo.claves[medio + 1:]
        nueva.hijos = nodo.hijos[medio + 1:]
        clave_media = nodo.claves[medio]  # la clave del medio sube al padre
        nodo.claves = nodo.claves[:medio]
        nodo.hijos = nodo.hijos[:medio + 1]
        return clave_media, nueva
