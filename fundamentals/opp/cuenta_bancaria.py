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
    
class CuentaBancaria:
    

    def __init__(self) -> None:
        pass


    def deposito(self, amount: float) -> None:
        pass

    
    def retiro(self, amount: float) -> None:
        pass


    def mostrar_info_cuenta(self) -> None:
        pass
    

    def generar_interes(self) -> None:
        pass