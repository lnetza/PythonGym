
class ReguladorDeLuz():
    def __init__(self):
        self.encendido = False
        self.intensidad = 0
    
    def encender(self):
        self.encendido = True
    
    def apagar(self):
        self.encendido = False
    
    def subirIntensidad(self):
        if self.intensidad < 10:
            self.intensidad += 1
    
    def bajarIntensidad(self):
        if self.intensidad > 0:
            self.intensidad -= 1
    
    def estado(self):
        print(f"Encendido: {self.encendido}, Intensidad: {self.intensidad}")

    
reguladorluz = ReguladorDeLuz()
reguladorluz.encender()
reguladorluz.subirIntensidad()
reguladorluz.subirIntensidad()
reguladorluz.estado()
