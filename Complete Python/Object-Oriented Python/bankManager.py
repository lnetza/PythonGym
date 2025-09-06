from accountBank import Cuenta

class BankManager:
    def __init__ (self):
        self.cuentas = {}
        self.idCuenta = 1

    def crearCuenta(self,nombre, saldo, contraseña):
        nuevaCuenta = Cuenta(nombre, saldo, contraseña)
        self.cuentas[self.idCuenta]= nuevaCuenta
        print(f"Cuenta creada exitosamente. ID de cuenta: {self.idCuenta}")
        self.idCuenta += 1
    
    def obtenerCuenta(self, idCuenta):
        return self.cuentas.get(idCuenta, None) 
    
    def depositar(self, idCuenta, monto, contraseña):
        cuenta = self.obtenerCuenta(idCuenta)
        if cuenta:
            cuenta.depositar(monto, contraseña)
        else:
            print("ID de cuenta incorrecto. No se puede realizar el depósito.")

    def retirar(self, idCuenta, monto, contraseña):
        cuenta = self.obtenerCuenta(idCuenta)
        if cuenta:
            cuenta.retirar(monto, contraseña)
        else:
            print("ID de cuenta incorrecto. No se puede realizar el retiro.")


miCuenta = BankManager()
miCuenta.crearCuenta("Juan Perez", 1000, "1234")
miCuenta.depositar(1, 500, "1234")
miCuenta.depositar(1, -200, "1234")
miCuenta.depositar(1, 300, "wrongpassword")
miCuenta.depositar(2, 300, "1234")
miCuenta.retirar(1, 20, "1234")
miCuenta.retirar(2, 20, "1234")