class TV():
    def __init__(self):
        self.prendida = False
        self.enSilencio = False
        self.listaCanales = [2,4,5,7,9,11,13]
        self.nCanales = len(self.listaCanales)
        self.canalInicial = 0
        self.VOLUMEN_MINIMO = 0
        self.VOLUMEN_MAXIMO = 10
        self.volumen = self.VOLUMEN_MAXIMO // 2
    
    def encenderApagar(self):
        self.prendida = not self.prendida
    
    def subirVolumen(self):
        if not self.prendida:
            return
        if self.enSilencio:
            self.enSilencio = False
        if self.volumen < self.VOLUMEN_MAXIMO:
            self.volumen += 1
    
    def bajarVolumen(self):
        if not self.prendida:
            return
        if self.enSilencio:
            self.enSilencio = False
        if self.volumen > self.VOLUMEN_MINIMO:
            self.volumen -= 1
    
    def subirCanal(self):
        if not self.prendida:
            return
        self.canalInicial += 1
        if self.canalInicial == self.nCanales:
            self.canalInicial = 0
    
    def bajarCanal(self):
        if not self.prendida:
            return
        self.canalInicial -= 1
        if self.canalInicial < 0:
            self.canalInicial = self.nCanales - 1
    
    def silenciar(self):
        if not self.prendida:
            return
        self.enSilencio = not self.enSilencio
    
    def asignarCanal(self, nuevoCanal):
        if nuevoCanal in self.listaCanales:
            self.canalInicial = self.listaCanales.index(nuevoCanal)

    def mostrarInformacion(self):
        print()
        print('TV Status:')
        if self.prendida:
            print(' TV esta encendida')
            print(' Canal:', self.listaCanales[self.canalInicial])
            if self.enSilencio:
                print(' El volumen es', self.volumen,'sonido muteado')
            else:
                print(' El volumen es', self.volumen)
        else:
            print(' La TV esta apagada')


oTV = TV()

oTV.encenderApagar()
oTV.mostrarInformacion()

oTV.subirCanal()
oTV.mostrarInformacion()
oTV.subirVolumen()
oTV.subirVolumen()
oTV.mostrarInformacion()

oTV.encenderApagar()
oTV.mostrarInformacion()
oTV.encenderApagar()
oTV.mostrarInformacion()

oTV.asignarCanal(5)
oTV.silenciar()
oTV.mostrarInformacion()

