from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Fruit']
    WEIGHT_INCREASE = 0.1

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 0.4

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Meat']
    WEIGHT_INCREASE = 0.3

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 1

    def make_sound(self):
        return 'ROAR!!!'
