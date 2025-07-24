
subastas = {}

def mazo():
    print("""
                            ___________
                                    /
                            )_______(
                            |"""""""|_.-._,.---------.,_.-._
                            |       | | |               | | ''-.
                            |       |_| |_             _| |_..-'
                            |_______| '-'''---------'' '-'
                            )"""""""(
                            /_________\
                        .-------------.
                        /_______________\
                        
    """)



def guardarSubasta(nombre,cantidad):
    subastas[nombre]=cantidad

def encontrarSubastaMayor():
    mayorSubasta = 0
    ganadorSubasta = ''
    for key, val in subastas.items():
        if val > mayorSubasta:
            mayorSubasta = val
            ganadorSubasta = key

    return f"La mayor subasta es de {ganadorSubasta} con un valor de ${mayorSubasta}"

respuesta = ''

mazo()

while respuesta.lower() != 'n':
    
    nombre = str(input("Teclea tu nombre:"))
    cantidad = int(input("Ingresa el monto: $"))

    guardarSubasta(nombre,cantidad)

    respuesta = str(input("Teclea 'Y' si hay otra persona que va ingresar su subasta, teclea 'N' si no hay:"))
    print("\n" * 100)
    


print(encontrarSubastaMayor())
