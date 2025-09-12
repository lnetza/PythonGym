from alumno import Alumno

class Escuela:
    def __init__(self):
        self.alumnos = {}
        self.idAlumno = 1
    
    def agregar_alumno(self, nombre, edad, grado):
        alumno = Alumno(nombre,edad,grado)
        self.alumnos[self.idAlumno] = alumno
        print(f"Se agregó el alumno con ID {self.idAlumno}\n")
        self.idAlumno += 1
    
    def mostrar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos en la escuela.\n")
            return
        for id, alumno in self.alumnos.items():
            print(f"ID {id}: {alumno.mostrar_info()}")

    def eliminar_alumno(self, id):
        if id in self.alumnos:
            self.alumnos.pop(id)
            print(f"Se eliminó el alumno con ID {id}\n")
        else:
            print(f"No se encontró un alumno con ID {id}\n")



print("Sistema de Gestión Escolar")
escuela = Escuela()

print("\n")
print("1) Agregar alumno")
print("2) Mostrar alumnos")
print("3) Eliminar alumno")


opcion  = input("Selecciona una opción:")

while True:
    if opcion == "1":
        nombre = input("Nombre del alumno:")
        edad = input("Edad del alumno:")
        grado = input("Grado:")
        escuela.agregar_alumno(nombre, edad, grado)
    if opcion == "2":
        escuela.mostrar_alumnos()
    if opcion == "3":
        id = int(input("ID del alumno a eliiminar:"))
        escuela.eliminar_alumno(id)

    opcion  = input("Selecciona una opción:")
