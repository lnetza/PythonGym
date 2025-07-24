
class Interruptor():
    def __init__(self):
        self.switchEncendido = False
    
    def encender(self):
        self.switchEncendido = True
    
    def apagar(self):
        self.switchEncendido = False
    
    def estado(self):
        print(self.switchEncendido)

#Crear una instancia de la clase Interruptor
oInterruptor = Interruptor()

oInterruptor.estado()  # Imprime el estado inicial (False)
oInterruptor.encender()  # Cambia el estado a True
oInterruptor.estado()  # Imprime el estado actualizado (True)
oInterruptor.apagar()  # Cambia el estado a False
oInterruptor.estado()  # Imprime el estado actualizado (False)
oInterruptor.encender()  # Cambia el estado a True
oInterruptor.estado()  # Imprime el estado actualizado (True)
# oInterruptor es una instancia de la clase Interruptor
# y puede ser utilizada para encender, apagar y verificar su estado.
# El método estado imprime el estado actual del interruptor.