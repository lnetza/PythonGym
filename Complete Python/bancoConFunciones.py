
titularCuenta =''
saldoCuenta = 0.0
passwordCuenta = ''


def assci():
    print("""
             _      _      _    
            oo\    oo\    oo\   
            (__)\  (__)\  (__)\  
            ---------------------- """)
    
def nuevaCuenta(titular, saldo, password):
    global titularCuenta, saldoCuenta, passwordCuenta
    titularCuenta = titular
    saldoCuenta = saldo
    passwordCuenta = password

def verInformacionCuenta():
    global titularCuenta, saldoCuenta, passwordCuenta
    print("Titular de la cuenta:", titularCuenta)
    print("Saldo de la cuenta:", saldoCuenta)
    print("Contraseña de la cuenta:", passwordCuenta)

def consultarSaldo(password):
    global saldoCuenta, passwordCuenta, titularCuenta
    if password == passwordCuenta:
        print("Saldo actual de la cuenta de", titularCuenta, "es:", saldoCuenta)
        assci()
    else:
        print("Contraseña incorrecta. No se puede consultar el saldo.")
        assci()

def retirarDinero(cantidad, password):
    global saldoCuenta, passwordCuenta

    if password == passwordCuenta:
        if cantidad > saldoCuenta:
            print("Fondos insuficientes, no es posible retirar esa cantidad.")
            assci()
        else:
            saldoCuenta -= cantidad
            print("Retiro exitoso. Nuevo saldo:", saldoCuenta)
            assci()
    else:
        print("Contraseña incorrecta.")
        assci()

def despositarDinero(cantidad):
    global saldoCuenta
    if cantidad < 0:
        print("No se puede depositar una cantidad negativa.")
        assci()
    else:
        saldoCuenta += cantidad
        print("Depósito exitoso. Nuevo saldo:", saldoCuenta)
        assci()


while True:
    print("Bienvenido al sistema bancario")
    print("1.Teclea (A)-Crear nueva cuenta")
    print("2.Teclea (B)-Ver información de la cuenta")
    print("3.Teclea (C)-Consultar saldo")
    print("4.Teclea (D)-Retirar dinero")
    print("5.Teclea (E)-Depositar dinero")
    print("6.Teclea (Q)-Salir")

    opcion = input("Seleccione una opción: ")

    if opcion.upper() == 'A':
        titular = input("Nombre del titular de la cuenta: ")
        saldo = int(input("Saldo inicial de la cuenta: "))
        password = input("Ingresa la contraseña de la cuenta: ")
        nuevaCuenta(titular, saldo, password)

    elif opcion.upper() == 'B':
        verInformacionCuenta()

    elif opcion.upper() == 'C':
        password = input("Ingresa la contraseña para consultar el saldo: ")
        consultarSaldo(password)
    
    elif opcion.upper() == 'D':
        password = input("Ingresa la contraseña de tu cuenta: ")
        cantidad = int(input("Cantidad a retirar: "))
        retirarDinero(cantidad, password)
    
    elif opcion.upper() == 'E':
        cantidad = int(input("Cantidad a depositar: "))
        despositarDinero(cantidad)

    elif opcion.upper() == 'Q':
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, intente de nuevo.")