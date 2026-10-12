"""Menu de consola: probar las 3 estructuras a mano."""

import random

from estudiante import Estudiante
from estructuras.abb import ABB
from estructuras.bmas import BPlus
from estructuras.lista import ListaEstudiantes


def main():
    print("Elija la estructura de almacenamiento:")
    print("  1) Lista ordenada")
    print("  2) Arbol binario de busqueda (ABB)")
    print("  3) Arbol B+")
    opcion = input("> ")

    fabricas = {"1": ListaEstudiantes, "2": ABB, "3": BPlus}
    sistema = fabricas.get(opcion, ListaEstudiantes)()

    while True:
        print("\n1) Insertar estudiante")
        print("2) Buscar por ID")
        print("3) Listar todos (orden ascendente de ID)")
        print("4) Generar N estudiantes aleatorios")
        print("5) Salir")
        opcion = input("> ")

        if opcion == "1":
            id_ = int(input("ID: "))
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            promedio = float(input("Promedio: "))
            sistema.insertar(Estudiante(id_, nombre, edad, promedio))
            print("Estudiante insertado.")
        elif opcion == "2":
            id_ = int(input("ID a buscar: "))
            estudiante = sistema.buscar(id_)
            print(estudiante if estudiante else "No encontrado.")
        elif opcion == "3":
            for estudiante in sistema.listar():
                print(estudiante)
        elif opcion == "4":
            n = int(input("Cuantos: "))
            ids = list(range(1, n + 1))
            random.shuffle(ids)
            for id_ in ids:
                sistema.insertar(Estudiante(id_, f"Estudiante {id_}", 20, 3.0))
            print(f"{n} estudiantes insertados.")
        elif opcion == "5":
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()
