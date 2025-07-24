

abcdrioNormal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
abcdrioDesplazado = []
posicionesAEncriptar =[]
posicionesADesencriptar =[]
textoEncriptado =[]
textoDesencriptado =[]

def desplazar(numeroDesplazamiento):
    numeroDesplazamiento = numeroDesplazamiento % 26

    for i in range(len(abcdrioNormal)):
        
        nuevoIndice = (i + numeroDesplazamiento) % len(abcdrioNormal)
        abcdrioDesplazado.append(abcdrioNormal[nuevoIndice])

def obtenerPosicionesAEcriptar(textoAEncriptar):
     for char in textoAEncriptar:
          if char in abcdrioNormal:
                posicionesAEncriptar.append(abcdrioNormal.index(char))

def obtenerPosicionesADesencriptar(textoADesencriptar):
     for char in textoADesencriptar:
          if char in abcdrioDesplazado:
                posicionesADesencriptar.append(abcdrioDesplazado.index(char))

def hacerEncriptado(posicionesAEncriptar):
    for i in posicionesAEncriptar:
            textoEncriptado.append(abcdrioDesplazado[i])

def hacerDesencriptado(posicionesADesencriptar):
    for i in posicionesADesencriptar:
            textoDesencriptado.append(abcdrioNormal[i])

def imprimirTextoEncriptado():
    for i in textoEncriptado:
        print(i, end="")
    print("")

def imprimirTextoDesencriptado():
    for i in textoDesencriptado:
        print(i, end="")
    print("")

def encriptar():
    numeroDesplazamiento = int(input("Numero de desplazamiento:"))
    textoAEncriptar = list(input("Texto:").upper())

    desplazar(numeroDesplazamiento)
    obtenerPosicionesAEcriptar(textoAEncriptar)
    hacerEncriptado(posicionesAEncriptar)
    imprimirTextoEncriptado()

def desencriptar():
    numeroDesplazamiento = int(input("Numero de desplazamiento:"))
    textoADesencriptar = list(input("Texto:").upper())

    desplazar(numeroDesplazamiento)
    obtenerPosicionesADesencriptar(textoADesencriptar)
    hacerDesencriptado(posicionesADesencriptar)
    imprimirTextoDesencriptado()


print("""
                              ██████╗ ██╗     ██╗██████╗ ███████╗
                             ██╔═══██╗██║     ██║██╔══██╗██╔════╝
                             ██║   ██║██║     ██║██║  ██║█████╗  
                             ██║   ██║██║     ██║██║  ██║██╔══╝  
                             ╚██████╔╝███████╗██║██████╔╝███████╗
                              ╚═════╝ ╚══════╝╚═╝╚═════╝ ╚══════╝

================================================================================
==                                                                            ==
==                        ¡Bienvenido al Cifrado!                             ==
==                                                                            ==

El Cifrado César es un tipo de cifrado por sustitución en el que cada letra de un texto
se reemplaza por otra letra que se encuentra un número fijo de posiciones más adelante
en el alfabeto. Por ejemplo, si se utiliza un desplazamiento de 3, la letra 'A' se convierte
en 'D', 'B' en 'E', y así sucesivamente. Este cifrado es fácil de implementar, pero también
es fácil de romper si se conoce el patrón de desplazamiento.
""")


continuar = 1

while continuar == 1:
    opcion = int(input("Teclea 1 para ENCRIPTAR, Teclea 2 para DESENCRIPTAR: "))

    
    while opcion != 1 and opcion != 2:
        print("Opción no válida.")
        opcion = int(input("Teclea 1 para ENCRIPTAR, Teclea 2 para DESENCRIPTAR: "))

    
    if opcion == 1:
        encriptar()
        textoEncriptado.clear()
        abcdrioDesplazado.clear()
        posicionesAEncriptar.clear()
    elif opcion == 2:
        desencriptar()
        textoDesencriptado.clear()
        abcdrioDesplazado.clear()
        posicionesADesencriptar.clear()

    continuar = int(input("Teclea 1 para continuar, otro número para salir: "))
