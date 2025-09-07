class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    
    def mostrar_info(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.anio}"