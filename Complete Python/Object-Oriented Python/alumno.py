class Alumno:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}"

    