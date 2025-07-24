import random

words = ['gato','perro','elefante','tigre','oso','chango','ardilla','cocodrilo','dinosaurio','hipopotamo']
"""
mono1 = [' ','+','-','-','+']
mono2 = [' ','|',' ',' ','|']
mono3 = [' ',' ',' ',' ','|']
mono4 = [' ',' ',' ',' ','|']
mono5 = [' ',' ',' ',' ','|']
mono6 = [' ',' ',' ',' ','|']
"""
mono = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]


listaCaracteres = []
palabraRandom = random.choice(words)


#print ("Palabra:",palabraRandom)


def mostrarEspacios(palabra,listaPalabra):
    for i in range(len(palabra)):
        listaPalabra.append('-')

def mostrarProgreso():
    for i in range(len(listaCaracteres)):
        print(f"{listaCaracteres[i]}", end='')
    print("\n")



def jugar():
    intentos=6

    mostrarEspacios(palabraRandom,listaCaracteres)
    print("Espacios de la palabra a adivinar")
    mostrarProgreso()

    while listaCaracteres != list(palabraRandom) and intentos > 0:
        print("\n")

        #for lista in [mono1,mono2,mono3,mono4,mono5,mono6]:
        #    print(' '.join(str(item) for item in lista))
        print(mono[intentos])

        print ("\nVidas restantes",intentos)
        

        adivinar = input("\nAdivia el nombre del animal:").lower()
        
        if adivinar in palabraRandom:
            for i in range(len(palabraRandom)):
                if adivinar == palabraRandom[i]:
                    listaCaracteres[i]=adivinar
        else:
            intentos=intentos-1

            print("Error, esa letra no forma parte del nombre del animal")
            """
            if intentos == 5:
                mono3[1]= ("0")
            if intentos == 4:
                mono4[0]= ("/")
            if intentos == 3:
                mono4[1]= ("|")
            if intentos == 2:
                mono4[2]= ("\\")
            if intentos == 1:
                mono6[0]= ("/")
            if intentos == 0:
                mono6[2]= ("\\")"""


        mostrarProgreso()

    if intentos == 0:
        print(mono[0])
        print("El nombre era:", palabraRandom)
        """
        for lista in [mono1,mono2,mono3,mono4,mono5,mono6]:
            print(' '.join(str(item) for item in lista))
        """
jugar()