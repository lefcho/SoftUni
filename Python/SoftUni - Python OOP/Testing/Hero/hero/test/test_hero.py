from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Test', 1, 2.5, 5.5)
        self.test_enemy = Hero('Test_enemy', 1, 2, 3)

    def test_init(self):
        self.assertEqual('Test', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(2.5, self.hero.health)
        self.assertEqual(5.5, self.hero.damage)

    def test_battle_when_enemy_hero_has_same_name_raise_ve(self):
        test_enemy = Hero('Test', 1, 2, 3)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(test_enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_negative_health_raise_ex(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.test_enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

        self.hero.health = 0
        with self.assertRaises(ValueError) as ve1:
            self.hero.battle(self.test_enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve1.exception))

    def test_enemy_hero_negative_health_raise_ve(self):
        self.test_enemy.health = -1
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.test_enemy)
        self.assertEqual("You cannot fight Test_enemy. He needs to rest", str(ve.exception))

        self.test_enemy.health = 0
        with self.assertRaises(ValueError) as ve1:
            self.hero.battle(self.test_enemy)
        self.assertEqual("You cannot fight Test_enemy. He needs to rest", str(ve1.exception))

    def test_draw_and_health_calculation(self):
        enemy = Hero('enemy', 1, 2.5, 5.5)
        result = self.hero.battle(enemy)
        self.assertEqual('Draw', result)
        self.assertEqual(-3, self.hero.health)

    def test_win_and_level_damage_health_calculations(self):
        enemy = Hero('enemy', 1, 1, 1)
        result = self.hero.battle(enemy)
        self.assertEqual('You win', result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(6.5, self.hero.health)
        self.assertEqual(10.5, self.hero.damage)

    def test_loss_and_level_damage_health_calculations(self):
        enemy = Hero('enemy', 1, 100, 2.5)
        result = self.hero.battle(enemy)
        self.assertEqual('You lose', result)
        self.assertEqual(enemy.level, 2)
        self.assertEqual(enemy.health, 99.5)
        self.assertEqual(enemy.damage, 7.5)

    def test_str_method(self):
        result = "Hero Test: 1 lvl\n" \
               "Health: 2.5\n" \
               "Damage: 5.5\n"
        self.assertEqual(result, str(self.hero))


if __name__ == '__main__':
    main()
