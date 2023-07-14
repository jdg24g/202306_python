div = "=" * 50

class Cuenta:
    """
    Clase que representa una cuenta bancaria.

    Atributos:
        interes (float): La tasa de interés aplicada a la cuenta.
        balance (float): El saldo actual de la cuenta.
        lista_instancias (list): Una lista que almacena todas las cuentas bancarias creadas.

    Métodos:
        __init__(interes, balance=0): Inicializa una nueva instancia de la clase Cuenta_Bancaria.
        depositar(monto): Deposita un monto específico en la cuenta.
        retiro(monto): Retira un monto específico de la cuenta si hay suficientes fondos.
        mostrar_info_cuenta(): Muestra información sobre el balance actual de la cuenta.
        generar_interes(): Calcula y agrega el rendimiento de interés al balance de la cuenta.
        imprimir_instancias(): Imprime la información de todas las cuentas bancarias creadas.
    """
    lista_instancias = []


    def __init__(self, interes, balance = 0):
        """
        Inicializa una nueva instancia de la clase Cuenta_Bancaria.

        Parámetros:
            interes (float): La tasa de interés aplicada a la cuenta.
            balance (float, opcional): El saldo inicial de la cuenta (predeterminado: 0).
        """
        self.interes = interes
        self.balance = balance
        Cuenta.lista_instancias.append(self)


    def depositar(self, monto):
        """
        Deposita un monto específico en la cuenta.

        Parámetros:
            monto (float): El monto a depositar en la cuenta.

        Retorna:
            self: La instancia actual de la clase Cuenta_Bancaria.
        """
        self.balance += monto
        return self
    

    def retiro(self,monto):
        """
        Retira un monto específico de la cuenta si hay suficientes fondos.

        Parámetros:
            monto (float): El monto a retirar de la cuenta.
        """
        if (self.balance - monto) > 0:
            self.balance -= monto
        else:
            print(f'Lo siento no tienes fondos suficientes en tu cuenta : {self.balance}')
        return self
    

    def mostrar_info_cuenta(self):
        """
        Muestra información sobre el balance actual de la cuenta.

        Retorna:
            self: La instancia actual de la clase Cuenta_Bancaria.
        """
        print(f'Balance: {self.balance}')
        return self
    

    def generar_interes(self):
        """
        Calcula y agrega el rendimiento de interés al balance de la cuenta.

        Retorna:
            self: La instancia actual de la clase Cuenta_Bancaria.
        """
        if self.balance > 0:
            self.balance += (self.balance * self.interes)
        else:
            print('No puedes generar interes porque tu balance es negativo')
        return self
    

    @classmethod
    def imprimir_instancias(cls):
        """
        Imprime la información de todas las cuentas bancarias creadas.
        """
        for instancia in cls.lista_instancias:
            instancia.mostrar_info_cuenta()

didier = Cuenta(0.2,100)
ruth = Cuenta(2.5,200)


print(div)
Cuenta.imprimir_instancias()
print(div)
didier.depositar(100).depositar(100).depositar(100).retiro(200).generar_interes().mostrar_info_cuenta()
print(div)
ruth.depositar(200).depositar(200).retiro(50).retiro(50).retiro(20).retiro(10).generar_interes().mostrar_info_cuenta()
print(div)