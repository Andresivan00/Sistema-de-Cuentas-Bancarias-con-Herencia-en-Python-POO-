# Sistema de Cuentas Bancarias con Herencia en Python (POO)

Ejemplo educativo y 100% funcional de **Programación Orientada a Objetos** que simula dos tipos de cuentas bancarias usando **herencia y sobreescritura de métodos**.

### Qué hace exactamente este código

- **Clase padre `Cuenta`**  
  Representa una cuenta bancaria básica:
  - Guarda saldo, número de consignaciones y retiros
  - Permite consignar y retirar dinero
  - Muestra el saldo y estadísticas

- **Clase hija `CuentaAhorro`** (hereda de `Cuenta`)  
  Simula una cuenta de ahorros real (como en Colombia):
  - Solo está **activa si el saldo es mayor a $10.000**
  - **No permite consignar ni retirar** si la cuenta está inactiva
  - Actualiza automáticamente su estado
  - Sobreescribe `consignar()`, `retirar()` e `imprimir()`
