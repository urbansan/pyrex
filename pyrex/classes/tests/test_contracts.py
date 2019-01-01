import os
import sys
import unittest
from datetime import date, timedelta
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from pyrex.classes.contracts import get_contract, Contract, contract_typologies
from pyrex.classes.trades import typologies


class TestContractFactory(unittest.TestCase):

    def test_spot(self):
        c1 = get_contract('spot','eur', 'pln', 1000, 5000)
        self.assertIsInstance(c1, Contract)
        self.assertIsInstance(c1, contract_typologies.Spot)
        self.assertEqual(len(c1.trades), 1)

    def test_outright(self):
        c1 = get_contract('outright', 'eur', 'pln', 1000, 5000, date.today())
        self.assertIsInstance(c1, Contract)
        self.assertIsInstance(c1, contract_typologies.Outright)
        self.assertEqual(len(c1.trades), 1)

    def test_fx_swap(self):
        c1 = get_contract('fx_swap', 'eur', 'pln', 1000, 5000, maturity1=date.today(),
                          maturity2=date.today() + timedelta(days=40))
        self.assertIsInstance(c1, Contract)
        self.assertIsInstance(c1, contract_typologies.FxSwap)
        self.assertEqual(len(c1.trades), 2)
        self.assertIsInstance(c1.trades[0], typologies.Spot)
        self.assertIsInstance(c1.trades[1], typologies.Outright)

    def test_raises(self):
        with self.assertRaises(ValueError):
            get_contract('typology does not exist')

if __name__ == '__main__':
    unittest.main()
