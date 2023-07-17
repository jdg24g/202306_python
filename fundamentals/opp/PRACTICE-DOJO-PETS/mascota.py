class Mascota():
    def __init__(self,name,tipo,golosinas,sonido) -> None:
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 100
        self.sonido = sonido

    def dormir(self):
        self.energia += 10
        return self


    def comer(self):
        self.salud += 5
        self.energia += 10
        return self

    def jugar(self):
        self.salud += 5
        return self

    def ruido(self):
        print(self.sonido)
        return self

class Gato(Mascota):
    def __init__(self, name, tipo, golosinas, sonido) -> None:
        super().__init__(name, tipo, golosinas, sonido)

class Perro(Mascota):
    def __init__(self, name, tipo, golosinas, sonido) -> None:
        super().__init__(name, tipo, golosinas, sonido)

chancho = Mascota('Puerco Araña','herbívoros',['zanahoria,lechuga,mandioca'],'oink')