class Alumno:
    def __init__(self, nombre, apellido, fecha_nacimiento, dni, tutor, notas=None, faltas=0, amonestaciones=0):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.dni = dni
        self.tutor = tutor
        self.notas = notas if notas else []
        self.faltas = faltas
        self.amonestaciones = amonestaciones

    def mostrar_datos(self):
        print(f"Alumno: {self.nombre} {self.apellido}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"DNI: {self.dni}")
        print(f"Tutor: {self.tutor}")
        print(f"Notas: {self.notas}")
        print(f"Faltas: {self.faltas}")
        print(f"Amonestaciones: {self.amonestaciones}")
        print("-" * 30)

    def a_linea(self):
        """Convierte el alumno a una línea de texto para guardar en archivo"""
        return f"{self.nombre};{self.apellido};{self.fecha_nacimiento};{self.dni};{self.tutor};{','.join(map(str,self.notas))};{self.faltas};{self.amonestaciones}"


def alumno_desde_linea(linea):
    """Función externa que reconstruye un Alumno desde una línea de texto"""
    partes = linea.strip().split(";")
    nombre, apellido, fecha, dni, tutor = partes[:5]
    notas = partes[5].split(",") if partes[5] else []
    notas = [int(n) for n in notas if n.isdigit()]
    faltas = int(partes[6])
    amonestaciones = int(partes[7])
    return Alumno(nombre, apellido, fecha, dni, tutor, notas, faltas, amonestaciones)
