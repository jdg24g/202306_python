class Usuario:
    """
    Representa a un usuario y su cuenta bancaria.

    Atributos:
        nombre (str): Nombre del usuario.
        cuenta (CuentaBancaria): Objeto de la clase CuentaBancaria que representa la cuenta del usuario.

    Métodos:
        __init__(nombre: str, cuenta: CuentaBancaria) -> None:
            Inicializa una instancia de Usuario con el nombre y la cuenta especificados.

        hacer_deposito(monto: float) -> None:
            Realiza un depósito en la cuenta del usuario por el monto especificado.

        hacer_retiro(monto: float) -> None:
            Realiza un retiro de la cuenta del usuario por el monto especificado.

        mostrar_balance_usuario() -> None:
            Muestra en pantalla el nombre del usuario y el balance actual de su cuenta.

        transferir_dinero(monto: float, usuario_destino: Usuario) -> Usuario:
            Transfiere la cantidad especificada al usuario destino, resta esa cantidad del balance del usuario actual,
            y muestra en pantalla los balances actualizados de ambos usuarios. Devuelve la instancia actual de Usuario.

    """

    def __init__(self, nombre: str, cuenta: "CuentaBancaria") -> None:
        self.nombre = nombre
        self.cuenta = cuenta

    def hacer_deposito(self, monto: float) -> None:
        """Realiza un depósito en la cuenta del usuario por el monto especificado."""
        self.cuenta.depositar(monto)

    def hacer_retiro(self, monto: float) -> None:
        """Realiza un retiro de la cuenta del usuario por el monto especificado."""
        self.cuenta.retirar(monto)

    def mostrar_balance_usuario(self) -> None:
        """Muestra en pantalla el nombre del usuario y el balance actual de su cuenta."""
        print(f"Usuario: {self.nombre}")
        self.cuenta.mostrar_info_cuenta()

    def transferir_dinero(self, monto: float, usuario_destino: "Usuario") -> "Usuario":
        """
        Transfiere la cantidad especificada al usuario destino, resta esa cantidad del balance del usuario actual,
        y muestra en pantalla los balances actualizados de ambos usuarios. Devuelve la instancia actual de Usuario.

        Args:
            monto (float): La cantidad de dinero a transferir.
            usuario_destino (Usuario): El usuario destino de la transferencia.

        Returns:
            Usuario: La instancia actual de Usuario.
        """
        self.cuenta.retirar(monto)
        usuario_destino.cuenta.depositar(monto)
        self.mostrar_balance_usuario()
        usuario_destino.mostrar_balance_usuario()
        return self

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
        """Realiza un depósito en la cuenta por el monto especificado."""
        self.balance += monto

    def retirar(self, monto: float) -> None:
        """
        Realiza un retiro de la cuenta por el monto especificado si hay suficientes fondos.
        Muestra un mensaje de error si no hay suficientes fondos en la cuenta.
        """
        if (self.balance - monto) >= 0:
            self.balance -= monto
        else:
            print("No tienes fondos suficientes en tu cuenta.")

    def mostrar_info_cuenta(self) -> None:
        """Muestra en pantalla el balance actual de la cuenta."""
        print(f"Balance: {self.balance}")

    def generar_interes(self) -> None:
        """Genera el interés correspondiente en la cuenta si el balance es mayor a cero."""
        if self.balance > 0:
            self.balance += (self.balance * self.interes)
        else:
            print("No puedes generar interés porque tu balance es negativo.")

    @classmethod
    def imprimir_instancias(cls) -> None:
        """Imprime en pantalla la información de todas las instancias de la clase CuentaBancaria creadas."""
        for instancia in cls.lista_instancias:
            instancia.mostrar_info_cuenta()


cuenta1 = CuentaBancaria(interes=0.05, balance=1000)
cuenta2 = CuentaBancaria(interes=0.03, balance=500)

usuario1 = Usuario("Didier Gimenez", cuenta1)
usuario2 = Usuario("Ruth Bogarin", cuenta2)

usuario1.hacer_deposito(500)
usuario2.hacer_retiro(200)

usuario1.mostrar_balance_usuario()
usuario2.mostrar_balance_usuario()

CuentaBancaria.imprimir_instancias()
