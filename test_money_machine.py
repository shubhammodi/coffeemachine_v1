import unittest
import unittest.mock
from money_machine import MoneyMachine

class TestMoneyMachine(unittest.TestCase):
    def setUp(self):
        self.money_machine = MoneyMachine()

    def test_is_transaction_successful(self):
        # Test with insufficient coins
        with unittest.mock.patch('builtins.input', side_effect=[0, 0, 0, 0]):
            self.assertFalse(self.money_machine.is_transaction_successful(1.0))

        # Test with exact amount of coins
        with unittest.mock.patch('builtins.input', side_effect=[2, 0, 0, 0]):
            self.assertTrue(self.money_machine.is_transaction_successful(0.5))

        # Test with more than enough coins
        with unittest.mock.patch('builtins.input', side_effect=[2, 1, 0, 0]):
            self.assertTrue(self.money_machine.is_transaction_successful(0.5))


    def test_process_coins(self):
        # Test case when all coin inputs are 0
        with unittest.mock.patch('builtins.input', side_effect=[0, 0, 0, 0]):
            self.assertEqual(self.money_machine.process_coins(), 0.0)
        
        # Test case when there is a mix of coins inserted
        with unittest.mock.patch('builtins.input', side_effect=[1, 1, 0, 2]):
            self.assertEqual(self.money_machine.process_coins(), 0.37)
