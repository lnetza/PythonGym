

listaCuentas = []

def error():
    print("""   
            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
           ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀            
        """)
    
def assci():
    print("""
             _      _      _    
            oo\    oo\    oo\   
            (__)\  (__)\  (__)\  
            ---------------------- """)
    
def nuevaCuenta(nombre, saldo, numeroCuenta, contraseña):
    cuenta = {
        'nombre': nombre,
        'saldo': saldo,
        'numeroCuenta': numeroCuenta,
        'contraseña': contraseña
    }
    listaCuentas.append(cuenta)


def informacionCuenta(contraseña):
    for cuenta in listaCuentas:
        if cuenta['contraseña'] == contraseña:
            return cuenta
    return None

def depositar(numeroCuenta,cantidad):
    for cuenta in listaCuentas:
        if cuenta['numeroCuenta'] == numeroCuenta:
            cuenta['saldo'] += cantidad
            return cuenta['saldo']
    return False

def retirar(contraseña, numeroCuenta, cantidad):
    for cuenta in listaCuentas:
        if cuenta['contraseña'] == contraseña and cuenta['numeroCuenta'] == numeroCuenta:
            if cuenta['saldo'] >= cantidad:
                cuenta['saldo'] -= cantidad
                return cuenta['saldo']
            else:
                return False
    return False


def mostrarCuentas():
    for cuenta in listaCuentas:
        print(f"Nombre: {cuenta['nombre']}, saldo: {cuenta['saldo']}, número de cuenta: {cuenta['numeroCuenta']}")



while True:
    print("1. Crear nueva cuenta")
    print("2. Consultar información de cuenta")
    print("3. Depositar dinero")
    print("4. Retirar dinero")
    print("5. Mostrar todas las cuentas")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese su nombre: ")
        saldo = float(input("Ingrese el saldo inicial: "))
        numeroCuenta = input("Ingrese el número de cuenta: ")
        contraseña = input("Ingrese una contraseña: ")
        nuevaCuenta(nombre, saldo, numeroCuenta, contraseña)
        print("Cuenta creada exitosamente.")
        assci()

    elif opcion == '2':
        contraseña = input("Ingrese su contraseña: ")
        cuenta = informacionCuenta(contraseña)
        if cuenta:
            print(f"Nombre: {cuenta['nombre']}, Saldo: {cuenta['saldo']}, Número de Cuenta: {cuenta['numeroCuenta']}")
            assci()
        else:
            print("Cuenta no encontrada.")

    elif opcion == '3':
        numeroCuenta = input("Ingrese el número de cuenta: ")
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        nuevoSaldo= depositar( numeroCuenta, cantidad)
        if nuevoSaldo:
            print(f"Depósito realizado exitosamente. Nuevo saldo: {nuevoSaldo}")
            assci()
        else:
            print("Error al realizar el depósito.")

    elif opcion == '4':
        contraseña = input("Ingrese su contraseña: ")
        numeroCuenta = input("Ingrese el número de cuenta: ")
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        nuevoSaldo = retirar(contraseña, numeroCuenta, cantidad)
        if nuevoSaldo:
            print("Retiro realizado exitosamente, nuevo saldo:", nuevoSaldo)
            assci()
        else:
            print("Error al realizar el retiro o saldo insuficiente.")

    elif opcion == '5':
        mostrarCuentas()
        assci()

    elif opcion == '6':
        break

    else:
        print("Opción no válida. Intente nuevamente.")
        assci()
