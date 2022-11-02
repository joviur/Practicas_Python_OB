class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Creado alumno", self.nombre, "con nota:", self.nota)

    def get_nombre(self):
        return self.nombre

    def get_nota(self):

        if self.nota >= 5:
            print("El alumno ha aprobado. La nota es:", self.nota)
        else:
            print("El alumno ha suspendido. La tona es:", self.nota)

a = Alumno("Josema", 4.2)

print(a.get_nombre())
a.get_nota()