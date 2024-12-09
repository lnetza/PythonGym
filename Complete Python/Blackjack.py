
import random

misCartas = []

cartasPC = []

def mostrar_intro():
    print("""
     
.------.           _     _            _    _            _    
|A_  _ |.         | |   | |          | |  (_)          | |   
|( \/ ).-----.    | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |    | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |    | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                           _/ |                
      '------'                         |____/
    """)

def suma(lista):

    sumaCartas = sum(lista)

    for i in range(len(lista)):
        if sumaCartas > 21 and lista[i] == 11:  
            lista[i] = 1

            sumaCartas = sum(lista)

    if sumaCartas == 21 and len(lista) == 2:
        return "Blackjack"
       
    return sumaCartas



def nuevaCartaJugador (jugador,cantidad):

    mazo = [11,2,3,4,5,6,7,8,9,10,10,10,10]


    if jugador =='persona':
        for i in range(0,cantidad):
            cartaAleatoria = random.choice(mazo)
            misCartas.append(cartaAleatoria)
        return misCartas
    if jugador =='pc':
        for i in range(0,cantidad):
            cartaAleatoria = random.choice(mazo)
            cartasPC.append(cartaAleatoria)
        return cartasPC[0]

def determinarGanador(pc, jugador):
    if pc == "Blackjack":
        return "¡Blackjack! Ganó la computadora."
    
    if jugador == "Blackjack":
        return "¡Blackjack! Ganó el jugador."
    
    if pc > 21 and jugador > 21:
        return "Ambos se pasaron de 21. Nadie gana."
    if pc > 21:
        return "¡Ganó el jugador! La computadora se pasó de 21."
    
    if jugador > 21:
        return "¡Ganó la computadora! El jugador se pasó de 21."

    if pc > jugador:
        return "¡Ganó la computadora!"
    if jugador > pc:
        return "¡Ganó el jugador!"
    
    
    return "¡Es un empate!"



respuesta = ''
while respuesta !='N':
    misCartas.clear()
    cartasPC.clear()
    
    mostrar_intro()
    print("\n"*2)   
    respuesta = input("Teclea 'Y' para jugar Blackjack 'N' para abandonar el juego:").upper()


    if respuesta == "Y":
        
        print("Tus cartas actuales:",nuevaCartaJugador('persona',2), "suma actual",suma(misCartas))
        print("Primera carta de la PC",nuevaCartaJugador('pc',2))
    
    if respuesta == "N":
        break
    continuar = ''

    total = suma(misCartas)
    totalPC = suma(cartasPC)

    if total ==  "Blackjack" or totalPC ==  "Blackjack":
        print("La última mano de la computadora:",cartasPC)
        print("Tu mano final:",misCartas)
        print(determinarGanador(pc=totalPC,jugador=total))
        
    else:
        while continuar !='N' and total<22:
            continuar = input("Teclea 'Y' para recibir otra carta, o 'n' para finalizar:").upper()
        
            if continuar == 'Y':
                print("Tus cartas actuales",nuevaCartaJugador('persona',1), "suma actual",suma(misCartas))
                print("Primera carta de la PC:",cartasPC[0])
                total= suma(misCartas)

                if total > 21:
                    
                    print(determinarGanador(pc=totalPC,jugador=total))
                    
            if continuar =='N':

                totalPC= suma(cartasPC)
                if totalPC <= 16:
                    while True:
                        nuevaCartaJugador('pc',1)
                        
                        totalPC = suma(cartasPC) 

                        if totalPC >=17 and totalPC <=21:
                            break
                        elif totalPC >21:
                            break
                
                print("La última mano de la computadora:",cartasPC, "puntos:",suma(cartasPC))
                print("Tu mano final:",misCartas, "puntos:",suma(misCartas))
                print(determinarGanador(pc=totalPC,jugador=total))
        
        


        