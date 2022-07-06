
class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def toString(self):
        return f"Nombre: {self.nombre} - Nota: {self.nota}"

    def resultado(self):
        if self.nota >= 6:
            return "aprobado"
        else:
            return "desaprobado"


a1 = Alumno("Juan", 8)
a2 = Alumno("Pedro", 5)

print(a1.toString())
print(a1.resultado())

print(a2.toString())
print(a2.resultado())


