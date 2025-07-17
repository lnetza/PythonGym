from diccionarioDatos import diccionarioArte, personasFamosas   
import random

personaConMasSeguidores ={
    "nombre":"",
    "seguidores":0,
    "descripcion":"",
    "pais":""   
}
score = 0
jugando = True

print(diccionarioArte[0]["intro"])

personasInciales=random.choices(personasFamosas, k=2)



def mostrarScore(score):
     print("Tu puntuación es:", score)

def actualizarPersonaConMasSeguidores(persona):
    personaConMasSeguidores["nombre"] = persona["nombre"]
    personaConMasSeguidores["seguidores"] = persona["seguidores"]
    personaConMasSeguidores["descripcion"] = persona["descripcion"]
    personaConMasSeguidores["pais"] = persona["pais"]

def excluirPersinaConMasSeguidores(personas, persona):
    personasDisponibles = []

    print("Se esta exlutendo a:", persona["nombre"],"de la lista de personas disponibles")
    for persona in personas:
        if persona["nombre"] != personaConMasSeguidores["nombre"]:
            personasDisponibles.append(persona)
            
    return personasDisponibles

print("Comparar A:",personasInciales[0]["nombre"],personasInciales[0]["descripcion"],"de",personasInciales[0]["pais"])

print(diccionarioArte[1]["vs"])

print("Contra B:",personasInciales[1]["nombre"],personasInciales[1]["descripcion"],"de",personasInciales[1]["pais"])

respuesta =input("¿Quién tiene más seguidores? A o B?").lower()

if respuesta == 'a':
      if personasInciales[0]["seguidores"] > personasInciales[1]["seguidores"]:
        actualizarPersonaConMasSeguidores(personasInciales[0])

        score += 1
        mostrarScore(score)
      elif personasInciales[1]["seguidores"] > personasInciales[0]["seguidores"]:
       
        print("¡Has elegido incorrectamente! La respuesta correcta es:", personasInciales[1]["nombre"])
        
elif respuesta == 'b':
        if personasInciales[1]["seguidores"] > personasInciales[0]["seguidores"]:
            actualizarPersonaConMasSeguidores(personasInciales[1])
            score += 1
            mostrarScore(score)
        elif personasInciales[0]["seguidores"] > personasInciales[1]["seguidores"]:
            print("¡Has elegido incorrectamente! La respuesta correcta es:", personasInciales[0]["nombre"])


while jugando:
    print("Comparar A:",personaConMasSeguidores["nombre"],personaConMasSeguidores["descripcion"],"de",personaConMasSeguidores["pais"])

    print(diccionarioArte[1]["vs"])

    diccionarioDePersonasDisponibles = excluirPersinaConMasSeguidores(personasFamosas, personaConMasSeguidores)
    personaNueva=random.choices(diccionarioDePersonasDisponibles , k=1)      

    print("Contra B:",personaNueva[0]["nombre"],personaNueva[0]["descripcion"],"de",personaNueva[0]["pais"]) 
    respuesta =input("¿Quién tiene más seguidores? A o B?").lower()
    
    if respuesta == 'a':
        if personaConMasSeguidores["seguidores"] > personaNueva[0]["seguidores"]:
            actualizarPersonaConMasSeguidores(personaNueva[0])
            score += 1
            mostrarScore(score)
            
        else:
            jugando = False
            print("¡Has elegido incorrectamente! La respuesta correcta es:", personaNueva[0]["nombre"])
            mostrarScore(score)
            break
    elif respuesta == 'b':
        if personaNueva[0]["seguidores"] > personaConMasSeguidores["seguidores"]:
            actualizarPersonaConMasSeguidores(personaNueva[0])
            score += 1
            mostrarScore(score)
        else:
            jugando = False
            print("¡Has elegido incorrectamente! La respuesta correcta es:", personaConMasSeguidores["nombre"])
            mostrarScore(score)
            break


