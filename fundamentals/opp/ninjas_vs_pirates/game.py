import random
div = "-#"*50+'\n'
class Personaje:
    def __init__(self,nombre,fuerza,velocidad) -> None:
        self.nombre = nombre
        self.vida = 100
        self.fuerza = fuerza
        self.velocidad = velocidad

    def mostrar_stats(self):
        if isinstance(self,Pirata):
            print(f'\033[34mNombre: {self.nombre}\nVida: {self.vida}\nFuerza: {self.fuerza}\nVelocidad: {self.velocidad}\033[0m')
            print(div)
        elif isinstance(self,Ninja):
            print(f'\033[32mNombre: {self.nombre}\nVida: {self.vida}\nFuerza: {self.fuerza}\nVelocidad: {self.velocidad}\033[0m')
            print(div)
    
    def calcular_dano(self):
        return self.fuerza + random.randint(1,10)
    
    def ataque(self,objetivo):
        dano = self.calcular_dano()
        objetivo.vida -= dano
        print(f'{self.nombre} ataco {objetivo.nombre} con {dano} daño')

        if objetivo.vida <= 0:
            print(div)
            print(f'\033[31m{objetivo.nombre} a sido derrotado')
            print(div)


class Pirata(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre,fuerza=15,velocidad=3)
    
    def calcular_dano(self):
        return super().calcular_dano() + 2.5

class Ninja(Personaje):
    def __init__(self,nombre):
        super().__init__(nombre,fuerza=12,velocidad=5)

    def calcular_dano(self):
        critico = 0.5
        if random.random() <= critico:
            print(f"\033[33mDaño Critico Aplicado\033[0m")
            return super().calcular_dano() * 2
        return super().calcular_dano()

def juego(p1,p2):
    while p1.vida >0 and p2.vida > 0:
        p1.ataque(p2)
        if p2.vida > 0:
            p2.mostrar_stats()
        if p2.vida > 0:
            p2.ataque(p1)
            if p1.vida > 0:
                p1.mostrar_stats()


michelangelo = Ninja("Genji")

jack_sparrow = Pirata("Junkrat")

juego(michelangelo,jack_sparrow)

