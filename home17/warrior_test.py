import unittest
from wars import Warrior, Swordsman, Archer, DarkArmy, LightArmy


class TestWarriors(unittest.TestCase):

    def setUp(self) -> None:
        self.army1 = DarkArmy()
        self.army2 = LightArmy()
        self.warrior1 = self.army1.train_swordsman("Peter", 100)
        self.warrior2 = self.army2.train_archer("Steve", 50)

    def tearDown(self) -> None:
        if self.warrior1 in self.army1.warriors:
            self.army1.warriors.remove(self.warrior1)

    def test_warrior_damage_change(self):
        Warrior.hit(self.warrior2)
        Warrior.hit(self.warrior1)

        self.assertEqual(self.warrior2.health, 35)
        self.assertEqual(self.warrior1.health, 75)

    def test_warrior_is_alive(self):
        Warrior.hit(self.warrior2)
        Warrior.hit(self.warrior2)
        Warrior.hit(self.warrior2)

        self.assertTrue(self.warrior2.is_alive, False)
        self.assertTrue(self.warrior1.is_alive, True)

    def test_remove_warrior_from_army(self):
        Warrior.hit(self.warrior2)
        Warrior.hit(self.warrior2)
        Warrior.hit(self.warrior2)
        Warrior.hit(self.warrior2)

        self.assertEqual(len(self.army2.warriors), 0)
        self.assertEqual(len(self.army1.warriors), 1)


        #check if warrior is in warriors list: self.assertNotIn(self.warrior1, self.army1.warriors)
        #check if warrior is dead: self.assertFalse(self.warrior1.is_alive)
