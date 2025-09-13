class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True


class Cliente:
    def __init__(self, nombre, apellido, idCliente=None):
        self.nombre = nombre
        self.apellido = apellido
        self.idCliente = idCliente

    
class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
    
    def __str__(self):
        return f"Reserva: {self.cliente.nombre} - Habitacion: {self.habitacion.numero} - Desde: {self.fecha_inicio} Hasta: {self.fecha_fin}"

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.clientes = []
        self.reservas = []
    
    def agregar_habitacion(self):
        numero = input("Numero habitacion:")
        tipo = input("Tipo habitacion:")
        precio = float(input("Precio habitacion:"))
        oHabitacion = Habitacion(numero, tipo, precio)
        self.habitaciones.append(oHabitacion)
        print("Habitacion agregada exitosamente.")
    
    def registrar_cliente(self):
        nombre = input("Nombre del cliente:")
        apellido = input("Apellido del cliente:")
        idCliente = input("ID del cliente (opcional):")
        oCliente = Cliente(nombre, apellido, idCliente)
        self.clientes.append(oCliente)
        print("Cliente registrado exitosamente.")
    
    def hacer_reserva(self):
        idCliente = input("ID del cliente para la reserva:")
        cliente = next((c for c in self.clientes if c.idCliente == idCliente), None)

        if not cliente:
            print("Cliente no encontrado. Por favor registre al cliente primero.")
            return None
        
        noHabitacion = input("Numero de habitacion a reservar:")
        habitacion = next((h for h in self.habitaciones if h.disponible and h.numero == noHabitacion), None)
        
        if not habitacion:
            print("Habitacion no disponible o no encontrada.")
            return None
        
        fecha_inicio = input("Fecha inicio (YYYY-MM-DD):")
        fecha_fin = input("Fecha fin (YYYY-MM-DD):")

        reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
        self.reservas.append(reserva)
        habitacion.disponible = False
        print("Reserva realizada exitosamente.")

        return reserva
                
    def ver_reservas(self):
        for reserva in self.reservas:
            print(reserva)
    
    def ver_habitaciones(self):
        for habitacion in self.habitaciones:
            estado = "Disponible" if habitacion.disponible else "No Disponible"
            print(f"Habitacion {habitacion.numero} - Tipo: {habitacion.tipo} - Precio: {habitacion.precio} - Estado: {estado}")


print("Sistema de Gestión de Hotel")
hotel = Hotel("Hotel Python")

while True:
    print("\nOpciones:")
    print("1. Agregar habitación")
    print("2. Registrar cliente")
    print("3. Hacer reserva")
    print("4. Ver reservas")
    print("5. Ver habitaciones")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        hotel.agregar_habitacion()
    elif opcion == '2':
        hotel.registrar_cliente()
    elif opcion == '3':
        reserva = hotel.hacer_reserva()
    elif opcion == '4':
        hotel.ver_reservas()
    elif opcion == '5':
        hotel.ver_habitaciones()
    elif opcion == '6':
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
