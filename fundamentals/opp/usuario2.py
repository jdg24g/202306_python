class Usuario:
    """Representa a un usuario con su nombre y balance.

    Atributos:
        nombre (str): El nombre del usuario.
        monto (float): El balance actual del usuario.

    Métodos:
        __init__(self, nombre: str) -> None:
            Inicializa una instancia de Usuario con el nombre proporcionado y un balance inicial de 0.

        cargar_dinero(self, monto: float) -> Usuario:
            Añade la cantidad especificada al balance del usuario y devuelve la instancia actual de Usuario.

        retirar_dinero(self, monto: float) -> Usuario:
            Resta la cantidad especificada al balance del usuario y devuelve la instancia actual de Usuario.

        mostrar_balance(self) -> None:
            Muestra en pantalla el nombre del usuario y su balance actual.

        transferir_dinero(self, monto: float, usuario_destino: Usuario) -> Usuario:
            Transfiere la cantidad especificada al usuario destino, resta esa cantidad del balance del usuario actual,
            y muestra en pantalla los balances actualizados de ambos usuarios. Devuelve la instancia actual de Usuario.
    """

    def __init__(self, nombre: str) -> None:
        """Inicializa una instancia de Usuario con el nombre proporcionado y un balance inicial de 0.

        Args:
            nombre (str): El nombre del usuario.
        """
        self.nombre = nombre
        self.monto = 0

    def cargar_dinero(self, monto: float) -> "Usuario":
        """Añade la cantidad especificada al balance del usuario y devuelve la instancia actual de Usuario.

        Args:
            monto (float): La cantidad de dinero a cargar.

        Returns:
            Usuario: La instancia actual de Usuario.
        """
        self.monto += monto
        return self

    def retirar_dinero(self, monto: float) -> "Usuario":
        """Resta la cantidad especificada al balance del usuario y devuelve la instancia actual de Usuario.

        Args:
            monto (float): La cantidad de dinero a retirar.

        Returns:
            Usuario: La instancia actual de Usuario.
        """
        self.monto -= monto
        return self

    def mostrar_balance(self) -> None:
        """Muestra en pantalla el nombre del usuario y su balance actual."""
        print(f"Usuario: {self.nombre}, Balance: {self.monto}")

    def transferir_dinero(self, monto: float, usuario_destino: "Usuario") -> "Usuario":
        """Transfiere la cantidad especificada al usuario destino, resta esa cantidad del balance del usuario actual,
        y muestra en pantalla los balances actualizados de ambos usuarios. Devuelve la instancia actual de Usuario.

        Args:
            monto (float): La cantidad de dinero a transferir.
            usuario_destino (Usuario): El usuario destino de la transferencia.

        Returns:
            Usuario: La instancia actual de Usuario.
        """
        self.monto -= monto
        usuario_destino.monto += monto
        self.mostrar_balance()
        usuario_destino.mostrar_balance()
        return self



francisco = Usuario("Francisco Boisier")
julio = Usuario("Julio Benitez")
jose = Usuario("Jose Webber")

francisco.cargar_dinero(100).cargar_dinero(200).cargar_dinero(50).retirar_dinero(45).mostrar_balance()

julio.cargar_dinero(1000).cargar_dinero(1000).retirar_dinero(500).retirar_dinero(300).mostrar_balance()

jose.cargar_dinero(1500).retirar_dinero(1000).retirar_dinero(5000).retirar_dinero(3000).mostrar_balance()


julio.transferir_dinero(400, francisco)