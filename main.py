from gestor import GestorEscuela
from alumno import Alumno

def menu():
    gestor = GestorEscuela()

    while True:
        print("\n--- Menú Escuela ---")
        print("1. Agregar alumno")
        print("2. Mostrar alumnos")
        print("3. Modificar alumno")
        print("4. Expulsar alumno")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            fecha = input("Fecha de nacimiento: ")
            dni = input("DNI: ")
            tutor = input("Tutor: ")
            notas = input("Notas separadas por coma (ej: 8,9,10): ")
            notas = [int(n) for n in notas.split(",")] if notas else []
            alumno = Alumno(nombre, apellido, fecha, dni, tutor, notas)
            gestor.agregar_alumno(alumno)

        elif opcion == "2":
            gestor.mostrar_alumnos()

        elif opcion == "3":
            dni = input("Ingrese DNI del alumno a modificar: ")
            campo = input("Campo a modificar (nombre, apellido, tutor, faltas, amonestaciones, notas): ")
            valor = input("Nuevo valor: ")
            if campo in ["faltas", "amonestaciones"]:
                valor = int(valor)
            elif campo == "notas":
                valor = [int(n) for n in valor.split(",")]
            gestor.modificar_alumno(dni, **{campo: valor})

        elif opcion == "4":
            dni = input("Ingrese DNI del alumno a expulsar: ")
            gestor.expulsar_alumno(dni)

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
