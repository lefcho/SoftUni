from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Test', 'test_type', 'test_sound')

    def test_init(self):
        self.assertEqual('Test', self.mammal.name)
        self.assertEqual('test_type', self.mammal.type)
        self.assertEqual('test_sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_making_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual('Test makes test_sound', result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_get_info(self):
        result = self.mammal.info()
        self.assertEqual('Test is of type test_type', result)


if __name__ == '__main__':
    main()