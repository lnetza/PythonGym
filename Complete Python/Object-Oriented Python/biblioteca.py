from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.idLibro = 1
    
    def agregar_libro(self, titulo, autor, anio):
        nuevoLibro = Libro(titulo, autor, anio)
        self.libros[self.idLibro] = nuevoLibro
        print(f"Se agregó el libro con ID {self.idLibro}")
        self.idLibro += 1
    
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        for id, libro in self.libros.items():
            print(f"ID {id}: {libro.mostrar_info()}")

    def eliminar_libro(self, id):
        if id in self.libros:
            del self.libros[id]
            print(f"Se eliminó el libro con ID {id}")
        else:
            print(f"No se encontró un libro con ID {id}")
    
    def buscar_por_autor(self, autor):
        encontrado = False
        for libro in self.libros.values():
            if libro.autor.lower() == autor.lower():
                print(f"{libro.mostrar_info()}")
                encontrado = True
        if not encontrado:
            print(f"No se encontraron libros del autor {autor}")
    
    def buscar_por_titulo(self, titulo):
        encontrado = False
        for libro in self.libros.values():
            if libro.titulo.lower() == titulo.lower():
                print(f"{libro.mostrar_info()}")
                encontrado = True
        if not encontrado:
            print(f"No se encontraron libros con el título {titulo}")
    
    def contar_libros(self):
        print(f"Total de libros en la biblioteca: {len(self.libros)}")
    

nuevoLibro = Biblioteca()
nuevoLibro.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
nuevoLibro.agregar_libro("1984", "George Orwell", 1949)
nuevoLibro.agregar_libro("To Kill a Mockingbird", "Harper Lee", 1960)
nuevoLibro.agregar_libro("The Great Gatsby", "F. Scott Fitzgerald", 1925)
nuevoLibro.mostrar_libros()
nuevoLibro.eliminar_libro(2)
nuevoLibro.mostrar_libros()
nuevoLibro.buscar_por_autor("Harper Lee")
nuevoLibro.buscar_por_titulo("1984")
nuevoLibro.buscar_por_titulo("The Great Gatsby")
nuevoLibro.contar_libros()
