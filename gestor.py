import os
from alumno import Alumno, alumno_desde_linea

class GestorEscuela:
    def __init__(self, archivo="alumnos.txt"):
        self.archivo = archivo
        self.alumnos = []
        self.cargar_datos()

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
        self.guardar_datos()

    def mostrar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos registrados.")
        for alumno in self.alumnos:
            alumno.mostrar_datos()

    def modificar_alumno(self, dni, **kwargs):
        for alumno in self.alumnos:
            if alumno.dni == dni:
                for clave, valor in kwargs.items():
                    if hasattr(alumno, clave):
                        setattr(alumno, clave, valor)
                self.guardar_datos()
                print("Alumno modificado con éxito.")
                return
        print("Alumno no encontrado.")

    def expulsar_alumno(self, dni):
        self.alumnos = [a for a in self.alumnos if a.dni != dni]
        self.guardar_datos()
        print("Alumno expulsado.")

    def guardar_datos(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for alumno in self.alumnos:
                f.write(alumno.a_linea() + "\n")

    def cargar_datos(self):
        self.alumnos = []
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    alumno = alumno_desde_linea(linea)
                    self.alumnos.append(alumno)
