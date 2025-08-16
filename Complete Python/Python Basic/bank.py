class Cuenta():
    def __init__(self, nombre, saldo, contraseña):
        self.nombre = nombre
        self.saldo = saldo
        self.contraseña = contraseña
    
    def depositar(self, monto, contraseña):
        if contraseña != self.contraseña:
            print("Contraseña incorrecta. No se puede realizar el depósito.")
            return
        if monto <= 0:
            print("El monto a depositar debe ser mayor que cero.")
            return
        
        self.saldo += monto
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo}")
    
    def retirar(self, monto, contraseña):
        if contraseña != self.contraseña:
            print("Contraseña incorrecta. No se puede realizar el retiro.")
            return
        if monto <= 0:
            print("El monto a retirar debe ser mayor que cero.")
        if monto > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
            return
        
        self.saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")
    
    def consultarSaldo(self, contraseña):
        if contraseña != self.contraseña:
            print("Contraseña incorrecta. No se puede consultar el saldo.")
            return
        print(f"Saldo actual: {self.saldo}")


cuenta1 = Cuenta("Jorge", 10000, "98987")
cuenta2 = Cuenta("Ana", 5000, "12345")
cuenta3 = Cuenta("Alejandra", 2000, "54321")
cuenta4 = Cuenta("Ivet", 3000, "67890")

cuenta1.consultarSaldo("98987")
cuenta1.depositar(500, "98987")
cuenta1.consultarSaldo("98987")
cuenta1.retirar(200, "98987")
cuenta1.consultarSaldo("98987")
print("---------------------------------")
cuenta2.consultarSaldo("12345")
cuenta2.depositar(1000, "12345")
cuenta2.consultarSaldo("12345")
cuenta2.retirar(6000, "12345")
cuenta2.consultarSaldo("12345")
print("---------------------------------")
cuenta3.consultarSaldo("54321")
cuenta3.depositar(300, "54321")
cuenta3.consultarSaldo("54321")
cuenta3.retirar(2500, "54321")
cuenta3.consultarSaldo("54321")
print("---------------------------------")
cuenta4.consultarSaldo("67890")
cuenta4.depositar(1500, "67890")
cuenta4.consultarSaldo("67890")
cuenta4.retirar(3500, "67890")
cuenta4.consultarSaldo("67890")

