
import random
PALOS_TUPLA = ("Diamantes ♦", "Corazones ♥", "Tréboles ♣", "Picas ♠")
RANGO_TUPLA = ("As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


"""Funcion que recibe la lista de cartas barajeadas y saca la última carta de la lista."""
def tomarCarta(cartas):
    carta = cartas.pop()  
    return carta 

"""Funcion que recibe la lista original de cartas, crea una copia y la guarda en la lista cartasBarajadas.
luego utiliza la función shuffle del módulo de random para barahar las cartas y finalmente retorna la lista barajada."""
def barajarCartas(listaCartas):
    cartasBarajadas = listaCartas.copy()
    random.shuffle(cartasBarajadas)
    return cartasBarajadas

print("Bienvenido al juego de Higher or Lower")
print("Debes elegir si la siguiente carta que se mostrará será mayor o menor que la actual.")
print("Acertar suma 20 puntos; equivocarse, pierdes 15 puntos.")
print("Tienes 50 puntos para empezar.")

"""
Este código itera sobre 2 tuplas una de PALOS_TUPLA y otra de RANGO_TUPLA.
Por cada Palo en PALOS_TUPLA itera sobre RANGO_TUPLA para crear un diccionario
el cual contiene el palo obtenido en la tupla PALOS_TUPLA, el nombre de la carta
obtenido en RANGO_TUPLA y el valor de la carta que es el indice + 1.
Finalmente, agrega cada diccionario a la lista listaDeCartas.
Con esto se genera una lista de todas las 52 cartas inglesas de una baraja.
"""
listaDeCartas = []
for palo in PALOS_TUPLA:
    for indice, valor in enumerate(RANGO_TUPLA):
        carta ={'palo':palo,'nombreCarta':valor,'valorCarta':indice + 1}
        listaDeCartas.append(carta)

score = 50

while True:
    cartasBarajadas = barajarCartas(listaDeCartas)
    cartaActual = tomarCarta(cartasBarajadas)
    print(f"\nLa carta actual es: {cartaActual['nombreCarta']} de {cartaActual['palo']}")
    break









