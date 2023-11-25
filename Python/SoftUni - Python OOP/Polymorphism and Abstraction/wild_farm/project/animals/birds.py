from project.animals.animal import Bird
from project.food import Vegetable, Meat, Fruit


class Owl(Bird):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    ALLOWED_FOODS = ['Vegetable', 'Meat', 'Seed', 'Fruit']
    WEIGHT_INCREASE = 0.35

    def make_sound(self):
        return "Cluck"


