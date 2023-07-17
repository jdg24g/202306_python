class Ninja():
    def __init__(self,nombre,apellido,mascotas,premio,comida_mascota) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida = comida_mascota
        

    def caminar(self):
        self.mascotas.jugar()
        return self


    def alimentar(self):
        self.mascotas.comer()
        return self

    
    def bañar(self):
        self.mascotas.ruido()
        return self