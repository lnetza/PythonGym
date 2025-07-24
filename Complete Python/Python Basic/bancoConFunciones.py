"""
En esta versión, se ha creado una función para cada una de las operaciones identificadas para una cuenta bancaria 
(Crear nueva cuenta, Ver información de la cuenta,Consultar saldo,Retirar dinero,Depositar dinero")y reorganizar el 
código para que el código principal contenga llamadas a las diferentes funciones.

Por ejemplo, si el usuario indica que desean hacer un depósito, el código ahora llama a una función llamada depositarDinero(), 
pasando el monto que se depositará y la contraseña de la cuenta.

Sin embargo, se observa la definición de alguna de estas funciones, por ejemplo, la función retirarDinero(), en el código se
usa las declaraciones globales para acceder (obtener o establecer) las variables que representan la cuenta. En Python, 
solo se requiere una declaración global si desea cambiar el valor de una variable global en una función. Sin embargo, se estan
usando aquí para dejar en claro que estas funciones se refieren a variables globales, incluso si solo están obteniendo un valor.

Como un principio de programación general, las funciones nunca deben modificar las variables globales. Una función solo debe 
usar datos que se transmitan, hacer cálculos basados en esos datos y potencialmente devolver un resultado o resultados. 
La función retirarDinero() en este programa funciona, pero viola esta regla modificando el valor de la variable global de 
consultarSaldo (además de acceder al valor de contraseña de la cuenta).
"""


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

def depositarDinero(cantidad):
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
        depositarDinero(cantidad)

    elif opcion.upper() == 'Q':
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, intente de nuevo.")