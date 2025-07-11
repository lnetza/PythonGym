print("Adivinha un número entre 1 y 100! hay 2 opciones: facil o dificil")

print("Teclea 1 para facil o 2 para dificil")
dificultad= int (input())

def numeroAleatorio():
    import random
    return random.randint(1, 100)

numeroGenerado = numeroAleatorio()

def adivinarNumero(intentos):
    numero = 0
    while numero != numeroGenerado and intentos > 0:
        numero= int(input("Introduce un número entre 1 y 100: "))
        if numero < numeroGenerado:
            print("El número es mayor")
            print("Te quedan", intentos - 1, "intentos")
        elif numero > numeroGenerado:
            print("El número es menor")
            print("Te quedan", intentos - 1, "intentos")
        else:
            print("¡Felicidades! Has adivinado el número.")
            break
        intentos -= 1

if dificultad == 1:
    print("Has elegido facil, tienes 10 intentos")
    adivinarNumero(10)
    print("El número aleatorio es: ", numeroGenerado)


if dificultad == 2:

    print("Has elegido dificil, tienes 5 intentos")
    adivinarNumero(5)
    print("El número aleatorio es: ", numeroGenerado)


