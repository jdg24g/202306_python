class Usuario:
    """
    Clase que representa a un usuario con un nombre y un balance.
    
    Atributos:
        nombre (str): El nombre del usuario.
        balance (float): El balance actual del usuario.

    Métodos:
        __init__(nombre):
            Inicializa una nueva instancia de la clase Usuario.
            Establece el nombre del usuario y establece el balance en 0.

        hacer_deposito(monto):
            Realiza un depósito en la cuenta del usuario.
            Aumenta el balance actual sumando el monto especificado.

        hacer_retiro(monto):
            Realiza un retiro de la cuenta del usuario.
            Disminuye el balance actual restando el monto especificado.
            Si el saldo es insuficiente, muestra un mensaje de error.

        mostrar_balance_usuario():
            Muestra el balance actual del usuario en pantalla.

        transferir_dinero(otro_usuario, monto):
            Transfiere una cantidad de dinero desde la cuenta del usuario actual hacia otro usuario.
            Disminuye el balance actual restando el monto especificado y aumenta el balance del otro usuario.
            Si el saldo es insuficiente, muestra un mensaje de error.
    """
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0

    def hacer_deposito(self, monto):
        """
        Realiza un depósito en la cuenta del usuario.

        Args:
            monto (float): El monto a depositar en la cuenta.

        Returns:
            devuelve la instancia del objeto self
        """
        self.balance += monto
        return self

    def hacer_retiro(self, monto):
        """
        Realiza un retiro de la cuenta del usuario.

        Args:
            monto (float): El monto a retirar de la cuenta.

        Returns:
            None
        """
        if self.balance >= monto:
            self.balance -= monto
            return self
        else:
            print(f"Saldo insuficiente para realizar el retiro. del {self.nombre}")

    def mostrar_balance_usuario(self):
        """
        Muestra el balance actual del usuario en pantalla.

        Returns:
            None
        """
        print(f"Balance de {self.nombre}: {self.balance}")

    def transferir_dinero(self, otro_usuario, monto):
        """
        Transfiere una cantidad de dinero desde la cuenta del usuario actual hacia otro usuario.

        Args:
            otro_usuario (Usuario): El objeto de la clase Usuario hacia donde se realizará la transferencia.
            monto (float): El monto a transferir.

        Returns:
            None
        """
        if self.balance >= monto:
            self.balance -= monto
            otro_usuario.balance += monto
            return self
        else:
            print("Saldo insuficiente para realizar la transferencia.")



# Crear usuarios
usuario1 = Usuario("Usuario1")
usuario2 = Usuario("Usuario2")
usuario3 = Usuario("Usuario3")


usuario1.hacer_deposito(100)
usuario1.hacer_deposito(50)
usuario1.hacer_deposito(20)
usuario1.hacer_retiro(30)
print("=============================")

usuario1.mostrar_balance_usuario()
print("=============================")


usuario2.hacer_deposito(200)
usuario2.hacer_deposito(75)
usuario2.hacer_retiro(100)
usuario2.hacer_retiro(50)

print("=============================")

usuario2.mostrar_balance_usuario()
print("=============================")


usuario3.hacer_deposito(50)
usuario3.hacer_retiro(20)
usuario3.hacer_retiro(30)
usuario3.hacer_retiro(25)

print("=============================")

usuario3.mostrar_balance_usuario()
print("=============================")


usuario1.transferir_dinero(usuario3, 50)


print("=============================")
usuario1.mostrar_balance_usuario()
print("=============================")
usuario3.mostrar_balance_usuario()
print("=============================")
