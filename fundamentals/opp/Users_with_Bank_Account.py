class Usuario:
    """
    Representa a un usuario y sus cuentas bancarias.

    Atributos:
        nombre (str): Nombre del usuario.
        cuentas (list): Lista de objetos de la clase CuentaBancaria que representan las cuentas del usuario.

    Métodos:
        __init__(nombre: str, cuentas: list) -> None:
            Inicializa una instancia de Usuario con el nombre y las cuentas especificadas.

        hacer_deposito(monto: float, num_cuenta: int) -> None:
            Realiza un depósito en la cuenta especificada del usuario por el monto especificado.

        hacer_retiro(monto: float, num_cuenta: int) -> None:
            Realiza un retiro de la cuenta especificada del usuario por el monto especificado.

        mostrar_balance_usuario() -> None:
            Muestra en pantalla el nombre del usuario y el balance actual de todas sus cuentas.

        transferir_dinero(monto: float, num_cuenta_origen: int, num_cuenta_destino: int) -> None:
            Transfiere la cantidad especificada de una cuenta del usuario a otra cuenta, muestra en pantalla los balances
            actualizados de ambas cuentas y el nombre del usuario.
    """

    def __init__(self, nombre: str, cuentas: list) -> None:
        self.nombre = nombre
        self.cuentas = cuentas

    def hacer_deposito(self, monto: float, num_cuenta: int) -> None:
        """
        Realiza un depósito en la cuenta especificada del usuario por el monto especificado.

        Args:
            monto (float): Monto a depositar.
            num_cuenta (int): Número de cuenta en la lista de cuentas del usuario.
        """
        cuenta = self.cuentas[num_cuenta]
        cuenta.depositar(monto)

    def hacer_retiro(self, monto: float, num_cuenta: int) -> None:
        """
        Realiza un retiro de la cuenta especificada del usuario por el monto especificado.

        Args:
            monto (float): Monto a retirar.
            num_cuenta (int): Número de cuenta en la lista de cuentas del usuario.
        """
        cuenta = self.cuentas[num_cuenta]
        cuenta.retirar(monto)

    def mostrar_balance_usuario(self) -> None:
        """
        Muestra en pantalla el nombre del usuario y el balance actual de todas sus cuentas.
        """
        print(f"Usuario: {self.nombre}")
        for i, cuenta in enumerate(self.cuentas):
            print(f"Cuenta {i+1}:")
            cuenta.mostrar_info_cuenta()

    def transferir_dinero(self, monto: float, num_cuenta_origen: int, num_cuenta_destino: int) -> None:
        """
        Transfiere la cantidad especificada de una cuenta del usuario a otra cuenta, muestra en pantalla los balances
        actualizados de ambas cuentas y el nombre del usuario.

        Args:
            monto (float): Monto a transferir.
            num_cuenta_origen (int): Número de cuenta de origen en la lista de cuentas del usuario.
            num_cuenta_destino (int): Número de cuenta de destino en la lista de cuentas del usuario.
        """
        cuenta_origen = self.cuentas[num_cuenta_origen]
        cuenta_destino = self.cuentas[num_cuenta_destino]

        cuenta_origen.retirar(monto)
        cuenta_destino.depositar(monto)

        print(f"Transferencia realizada por el usuario: {self.nombre}")
        print(f"Balance actualizado de Cuenta {num_cuenta_origen+1}:")
        cuenta_origen.mostrar_info_cuenta()
        print(f"Balance actualizado de Cuenta {num_cuenta_destino+1}:")
        cuenta_destino.mostrar_info_cuenta()


class CuentaBancaria:
    """
    Representa una cuenta bancaria.

    Atributos:
        interes (float): Interés de la cuenta.
        balance (float): Balance de la cuenta.
        lista_instancias (list): Lista de instancias de la clase.

    Métodos:
        __init__(interes: float, balance: float = 0) -> None:
            Inicializa una instancia de CuentaBancaria con el interés y el balance especificados.

        depositar(monto: float) -> None:
            Realiza un depósito en la cuenta por el monto especificado.

        retirar(monto: float) -> None:
            Realiza un retiro de la cuenta por el monto especificado.

        mostrar_info_cuenta() -> None:
            Muestra en pantalla el balance actual de la cuenta.

        generar_interes() -> None:
            Genera el interés correspondiente en la cuenta si el balance es mayor a cero.

        @classmethod
        imprimir_instancias() -> None:
            Imprime en pantalla la información de todas las instancias de la clase CuentaBancaria creadas.
    """
    lista_instancias = []

    def __init__(self, interes: float, balance: float = 0) -> None:
        self.interes = interes
        self.balance = balance
        CuentaBancaria.lista_instancias.append(self)

    def depositar(self, monto: float) -> None:
        """
        Realiza un depósito en la cuenta por el monto especificado.

        Args:
            monto (float): Monto a depositar.
        """
        self.balance += monto

    def retirar(self, monto: float) -> None:
        """
        Realiza un retiro de la cuenta por el monto especificado.

        Args:
            monto (float): Monto a retirar.
        """
        if (self.balance - monto) >= 0:
            self.balance -= monto
        else:
            print("No tienes fondos suficientes en tu cuenta.")

    def mostrar_info_cuenta(self) -> None:
        """
        Muestra en pantalla el balance actual de la cuenta.
        """
        print(f"Balance: {self.balance}")

    def generar_interes(self) -> None:
        """
        Genera el interés correspondiente en la cuenta si el balance es mayor a cero.
        """
        if self.balance > 0:
            self.balance += (self.balance * self.interes)
        else:
            print("No puedes generar interés porque tu balance es negativo.")

    @classmethod
    def imprimir_instancias(cls) -> None:
        """
        Imprime en pantalla la información de todas las instancias de la clase CuentaBancaria creadas.
        """
        for instancia in cls.lista_instancias:
            instancia.mostrar_info_cuenta()


cuenta1 = CuentaBancaria(interes=0.05, balance=1000)
cuenta2 = CuentaBancaria(interes=0.03, balance=500)
cuenta3 = CuentaBancaria(interes=0.02, balance=200)

usuario1 = Usuario("Didier Gimenez", [cuenta1, cuenta2, cuenta3])

usuario1.hacer_deposito(500, 0)
usuario1.hacer_retiro(200, 1)
usuario1.transferir_dinero(300, 1, 2)

usuario1.mostrar_balance_usuario()
