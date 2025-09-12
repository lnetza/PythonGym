from tarea import Tarea

class GestorTarea:
    def __init__(self):
        self.tareas = {}
        self.idTarea = 1
    
    def crear_tarea(self, titulo, descripcion, estado, prioridad):
        tarea= Tarea(titulo, descripcion, estado, prioridad)
        self.tareas[self.idTarea] = tarea
        print(f"Se creó la tarea con ID {self.idTarea}\n")
        self.idTarea += 1
    
    def mostrar_tareas(self):
        for id, tarea in self.tareas.items():
            print(f"ID {id}: {tarea}\n")

    def eliminar_tarea(self, id):
        if id in self.tareas:
            del self.tareas[id]
            print(f"Se eliminó la tarea con ID {id}\n")
        else:
            print(f"No se encontró una tarea con ID {id}\n")
    
    def actualizar_status(self, id, nuevo_estado):
        if id in self.tareas:
            self.tareas[id].estado = nuevo_estado
            print(f"Se actualizó el estado de la tarea con ID {id} a {nuevo_estado}\n")
        else:
            print(f"No se encontró una tarea con ID {id}\n")
    

tarea = GestorTarea()

print("Sistema de Gestión de Tareas")
print("1) Crear tarea")
print("2) Mostrar tareas")
print("3) Eliminar tarea")
print("4) Actualizar estado de tarea")

opcion  = input("Selecciona una opción:")

while True:
    if opcion == "1":
        titulo = input("Titulo de la tarea:")
        descripcion = input("Descripción de la tarea:")
        estado = input("Estado de la tarea (pendiente/progreso/completada):")
        prioridad = input("Prioridad de la tarea (baja/media/alta):")
        tarea.crear_tarea(titulo, descripcion, estado, prioridad)
    elif opcion == "2":
        tarea.mostrar_tareas()
    elif opcion == "3":
        id = int(input("Cual es el ID de la tarea?:"))
        tarea.eliminar_tarea(id)
    elif opcion == "4":
        id = int(input("Cual es el ID de la tarea?:"))
        nuevo_estado = input("Nuevo estado de la tarea (pendiente/progreso/completada):")
        tarea.actualizar_status(id, nuevo_estado)
    elif opcion.lower() == "salir":
        break
    else:
        print("Opción inválida")
    
    opcion = input("Selecciona una opción (o 'salir' para terminar): ")
