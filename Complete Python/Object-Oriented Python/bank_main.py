#Usando listas de cuentas
from bank import Cuenta

listaCuentas = []

oCuenta= Cuenta("Juan Perez", 1000, "1234")
listaCuentas.append(oCuenta)

oCuenta= Cuenta("Maria Lopez", 2000, "5678")
listaCuentas.append(oCuenta)

oCuenta= Cuenta("Carlos Gomez", 3000, "9101")
listaCuentas.append(oCuenta)


# Imprimir los datos de las cuentas

listaCuentas[0].depositar(500, "1234")
listaCuentas[0].consultarSaldo("1234")
listaCuentas[1].depositar(1000, "5678")
listaCuentas[1].consultarSaldo("5678")
listaCuentas[2].retirar(1500, "9101")
listaCuentas[2].consultarSaldo("9101")
