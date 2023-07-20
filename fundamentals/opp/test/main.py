import random

class Character:
    def __init__(self, nombre, fuerza, velocidad, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        self.vida = vida

    def show_stats(self):
        print(f"Nombre: {self.nombre}\nFuerza: {self.fuerza}\nVelocidad: {self.velocidad}\nVida: {self.vida}\n")

    def attack(self, target):
        damage = self.calculate_damage()
        target.vida -= damage
        print(f"{self.nombre} ataco {target.nombre} con {damage} daño!")
        if target.vida <= 0:
            print(f"{target.nombre} ha sido derrotado")

    def calculate_damage(self):
        return self.fuerza + random.randint(1, 10)  # Add some randomness to the damage


class Pirate(Character):
    def __init__(self, name):
        super().__init__(name, fuerza=15, velocidad=3, vida=100)

    def calculate_damage(self):
        return super().calculate_damage() + 5  # Pirates deal additional damage


class Ninja(Character):
    def __init__(self, name):
        super().__init__(name, fuerza=10, velocidad=5, vida=100)

    def calculate_damage(self):
        crit_chance = 0.3  # 30% chance of a critical hit
        if random.random() <= crit_chance:
            print("Critico!")
            return super().calculate_damage() * 2
        return super().calculate_damage()


def battle(p1, p2):
    while p1.vida > 0 and p2.vida > 0:
        p1.attack(p2)
        p2.show_stats()
        if p2.vida > 0:
            p2.attack(p1)
            p1.show_stats()

michelangelo = Ninja("Michelangelo")
jack_sparrow = Pirate("Jack Sparrow")

battle(michelangelo, jack_sparrow)
