import unittest
from wars import Swordsman, DarkArmy, LightArmy, Archer


class TestArmy(unittest.TestCase):

    def setUp(self) -> None:
        self.army1 = DarkArmy()
        self.army2 = LightArmy()
        self.warrior1 = self.army1.train_swordsman("Peter", 100)
        self.warrior2 = self.army2.train_archer("Steve", 10)

    def test_train_warrior_belongs_to_right_class(self):

        self.assertIsInstance(self.warrior1, Swordsman)
        self.assertIsInstance(self.warrior2, Archer)

    def test_army_if_new_train(self):

        old = len(self.army1.warriors)
        self.army1.train_swordsman("Peter", 100)
        new = len(self.army1.warriors)
        self.assertTrue(old + 1, new)

    def test_army_repr(self):
        self.assertEqual(repr(self.army1), "dark army")
        self.assertEqual(repr(self.army2), "light army")
