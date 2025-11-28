class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo      # Saldo inicial de la cuenta
        self._numCos = 0         # Contador de consignaciones
        self._numRet = 0         # Contador de retiros

    def consignar(self, monto):
        self._saldo += monto     # Suma el monto al saldo
        self._numCos += 1        # Aumenta el contador de consignaciones

    def retirar(self, monto):
        if monto > self._saldo:
            print("Saldo insuficiente")
        else:
            self._saldo -= monto # Resta el monto
            self._numRet += 1    # Aumenta el contador de retiros

    def getSaldo(self):
        return self._saldo       # Devuelve el saldo actual

    def imprimir(self):
        return f"""Saldo: {self._saldo}
Numero de consignaciones: {self._numCos}
Numero de retiros: {self._numRet}"""


# CLASE HIJA CORREGIDA
class CuentaAhorro(Cuenta):
    def __init__(self, saldo):
        super().__init__(saldo)
        # Una cuenta de ahorros está activa solo si tiene más de 10.000
        if self._saldo > 10000:
            self._activa = True
            print("Cuenta de ahorros creada y ACTIVA")
        else:
            self._activa = False
            print("Cuenta de ahorros creada pero INACTIVA (saldo menor a 10.000)")

    # Método para verificar si está activa (actualiza el estado cada vez)
    def esta_activa(self):
        if self._saldo > 10000:    # Regla típica colombiana de cuentas de ahorro
            self._activa = True
        else:
            self._activa = False
        return self._activa

    # SOBREESCRITURA DE consignar
    def consignar(self, monto):
        if self.esta_activa():              # Solo permite consignar si está activa
            super().consignar(monto)        # ¡Ahora SÍ suma! (antes restaba)
            print(f"Consignación exitosa de {monto}")
        else:
            print("Cuenta inactiva → no se puede consignar")

    # SOBREESCRITURA DE retirar
    def retirar(self, monto):
        if self.esta_activa():              # Solo permite retirar si está activa
            super().retirar(monto)          # Llama al método retirar del padre
            print(f"Retiro exitoso de {monto}")
        else:
            print("Cuenta inactiva → no se puede retirar")

    # Mostrar información completa
    def imprimir(self):
        estado = "SÍ" if self._activa else "NO"
        return f"""¿Cuenta activa? {estado}
{super().imprimir()}"""


# ===== PRUEBA CORRECTA =====
print("=== Probando clase Cuenta normal ===")
c = Cuenta(9000000)
print(c.imprimir())
c.consignar(500000)
print("Nuevo saldo:", c.getSaldo())      # ¡Ahora con paréntesis!
c.retirar(500000)
print("Nuevo saldo:", c.getSaldo())
print(c.imprimir())

print("\n=== Probando CuentaAhorro ===")
ca = CuentaAhorro(15000)       # Más de 10.000 → activa
print(ca.imprimir())
ca.consignar(5000)
ca.retirar(3000)
print(ca.imprimir())

print("\n=== Cuenta inactiva ===")
ca2 = CuentaAhorro(5000)       # Menos de 10.000 → inactiva
ca2.consignar(10000  )         # Intentará consignar pero no dejará
ca2.retirar(2000)              # No dejará retirar