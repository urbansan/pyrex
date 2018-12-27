import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from pyrex.classes.contracts import ContractFactory, Contract, contract_typologies


class TestContractFactory(unittest.TestCase):

    def test_spot(self):
        c1 = ContractFactory('spot', nominal=1000, currency='eur')
        self.assertIsInstance(c1, Contract)
        self.assertIsInstance(c1, contract_typologies.Spot)
        self.assertEqual(len(c1.trades), 1)

    def test_outright(self):
        c1 = ContractFactory('outright', nominal=1000, currency='eur')
        self.assertIsInstance(c1, Contract)
        self.assertIsInstance(c1, contract_typologies.Outright)
        self.assertEqual(len(c1.trades), 1)

    def test_fx_swap(self):
        c1 = ContractFactory('fx_swap', nominal=1000, currency='eur')
        self.assertIsInstance(c1, Contract)
        self.assertIsInstance(c1, contract_typologies.FxSwap)
        self.assertEqual(len(c1.trades), 2)


    def test_raises(self):
        with self.assertRaises(ValueError):
            ContractFactory('typology does not exist')

if __name__ == '__main__':
    unittest.main()
