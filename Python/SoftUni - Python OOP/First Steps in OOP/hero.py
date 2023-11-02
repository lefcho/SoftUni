class Hero:
    def __init__(self, name: str, health: float):
        self.name = name
        self.health = health

    def defend(self, demaage: float):
        self.health -= demaage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, ammount: float):
        self.health += ammount

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
