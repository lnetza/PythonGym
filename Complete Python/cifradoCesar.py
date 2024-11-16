

listaOriginal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
listaDesplazada = []
posicionesAEncriptar =[]
textoEncriptado =[]

def desplazar(numeroDesplazamiento):
    numeroDesplazamiento = numeroDesplazamiento % 26

    for i in range(len(listaOriginal)):
        
        nuevoIndice = (i + numeroDesplazamiento) % len(listaOriginal)
        listaDesplazada.append(listaOriginal[nuevoIndice])

def obtenerPosicionesAEcriptar(textoAEncriptar):
     for i in range(len(textoAEncriptar)):
        for z in range(len(listaOriginal)):
            if textoAEncriptar[i] == listaOriginal[z]:
                posicionesAEncriptar.append(z)

def hacerEncriptado(posicionesAEncriptar):
    for i in range(len(posicionesAEncriptar)):
            textoEncriptado.append(listaDesplazada[posicionesAEncriptar[i]])


def imprimirTextoEncriptado():
    print(textoEncriptado)


def encriptar():
    numeroDesplazamiento = int(input("Numero de desplazamiento:"))
    textoAEncriptar = list(input("Texto:").upper())

    desplazar(numeroDesplazamiento)
    obtenerPosicionesAEcriptar(textoAEncriptar)
    hacerEncriptado(posicionesAEncriptar)
    imprimirTextoEncriptado()

encriptar()