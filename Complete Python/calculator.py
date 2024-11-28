def sumar(n1,n2):
    return n1 + n2

def restar(n1,n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2

def dividir(n1,n2):
    return n1 / n2




def calcular():

    numero = int(input("Ingresa el numero:"))

    acumulador = numero
    respuesta =''

    operaciones = {
                    1:sumar,
                    2:restar,
                    3:multiplicar,
                    4:dividir
                }
    
    while True:
        print(""" 
            1) +Sumar
            2) -Restar
            3) *Multiplicar
            4) /Dividir
            """)
        opcion = int(input("Selecciona la opcion:"))
        
        if opcion in operaciones:
            numerorestante = int(input("Ingresa el numero:"))
            acumulador = operaciones[opcion](acumulador, numerorestante)
            print(acumulador)
                
            
            
            print("Quieres continuar con el resultado", acumulador, "teclea 'y',")
            respuesta = input("de lo contrario teclea 'n' para una nueva operacion, opcion 'x' para finalizar:")
       
        if respuesta.lower() == 'n':
            print("\n" * 20)
            return calcular()
        if respuesta.lower() == 'x':
            break

calcular()


