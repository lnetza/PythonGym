#uso de diccionarios para almacenar objetos

from bank import Cuenta

diccionarioCuentas = {}
numeroCuenta = 0
print("")
while True:
    print("1. Crear cuenta")
    print("2. Consultar saldo")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Salir")

    opcion = input("Selecciona una opción:")
    if opcion == "1":
        titular = input("Ingresa el nombre del titular de la cuenta:")
        saldo = float(input("Ingresa el saldo inicial de la cuenta:"))
        contraseña = input("Ingresa la contraseña de la cuenta:")
        oCuenta = Cuenta(titular, saldo, contraseña)
        diccionarioCuentas[numeroCuenta] = oCuenta
        print(f"Cuenta creada con número {numeroCuenta}")
        numeroCuenta += 1
    if opcion == "2":
        cuenta = int(input("Ingresa el número de cuenta:"))
        contraseña = input("Ingresa la contraseña:")

        oCuenta = diccionarioCuentas[cuenta]
        saldo = oCuenta.consultarSaldo(contraseña)
        if saldo is not None:
            print(f"Saldo de la cuenta {cuenta}: {saldo}")
    if opcion == "3":
        cuenta = int(input("Numero de cuenta:"))
        monto = float(input("Monto a depositar:"))
        contraseña = input("Contraseña:")
        if cuenta not in diccionarioCuentas:
            print("Cuenta no encontrada.")
            continue
        oCuenta = diccionarioCuentas[cuenta]
        depositar = oCuenta.depositar(monto,contraseña)
    if opcion == "4":
        cuenta = int(input("Numero de cuenta:"))
        monto = float(input("Monto a retirar:"))
        contraseña = input("Contraseña:")
        if cuenta not in diccionarioCuentas:
            print("Cuenta no encontrada.")
            continue
        oCuenta = diccionarioCuentas[cuenta]
        retirar = oCuenta.retirar(monto,contraseña)
    if opcion == "5":
        break
