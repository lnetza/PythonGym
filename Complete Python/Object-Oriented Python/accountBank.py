class Cuenta:
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
