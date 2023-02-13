import unittest
from menu import Menu, MenuItem

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()

    def test_get_items(self):
        self.assertEqual(self.menu.get_items(), "espresso/latte/cappuccino/")

    def test_find_drink_exists(self):
        drink = self.menu.find_drink("espresso")
        self.assertIsInstance(drink, MenuItem)
        self.assertEqual(drink.name, "espresso")
        self.assertEqual(drink.ingredients, {"water": 50, "milk": 0, "coffee": 18})
        self.assertEqual(drink.cost, 1.5)

    def test_find_drink_not_exists(self):
        drink = self.menu.find_drink("tea")
        self.assertIsNone(drink)

if __name__ == '__main__':
    unittest.main()