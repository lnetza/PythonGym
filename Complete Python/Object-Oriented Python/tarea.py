class Tarea:
    def __init__ (self, titulo, descripcion, estado, prioridad):
        self.descripcion = descripcion
        self.titulo = titulo
        self.estado = estado
        self.prioridad = prioridad

    def __str__(self):
        return f"Tarea: {self.titulo}, Descripción: {self.descripcion}, Estado: {self.estado}, Prioridad: {self.prioridad}"