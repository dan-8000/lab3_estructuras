from dataclasses import dataclass


@dataclass
class Estudiante:
    """Un registro de estudiante: lo minimo que pide el enunciado."""
    id: int          # numero unico de matricula
    nombre: str
    edad: int
    promedio: float
