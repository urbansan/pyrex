import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from pyrex import Trade, Contract
from pyrex.classes.contract import TradeList, ContractFactory

# print(__file__)

class TestTradeInit(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_typology_not_in_list(self):
        with self.assertRaises(ValueError):
            Trade('hadouken', 'eur', rate=0.1, nominal=10_100_999)

    def test_spot_init(self):
        Trade('spot', currency='eur', rate=0.1, nominal=10_100_999)
        Trade('spot', currency='eur', rate='0.1', nominal='10000')
        Trade('spot', currency='eur', rate=0.1, nominal='10000.0')
        with self.assertRaises(ValueError):
            Trade('spot', currency='eur', rate='random_string', nominal='10000.0')


class TestContractFactory(unittest.TestCase):

    def test_create_spot(self):
        spot = ContractFactory('spot', nominal=1000, currency='eur')
        self.assertIsInstance(spot, Contract)

    def test_create_outright(self):
        outright = ContractFactory('outright', nominal=1000, currency='eur')
        self.assertIsInstance(outright, Contract)

    def test_raises(self):
        with self.assertRaises(ValueError):
            ContractFactory('typology does not exist')



class TestTradeList(unittest.TestCase):

    def setUp(self):
        self.trades = [Trade('spot', 'eur', 10, 20), Trade('spot', 'eur', 20, 10), Trade('outright', 'eur', 11, 10)]
        self.random_list = [1, 2, 3, 'trade']
        self.trade_list = TradeList()

    def tearDown(self):
        del self.trades
        del self.trade_list

    def test_special_methods(self):
        self.trade_list += self.trades
        self.trade_list = self.trade_list + self.trades
        self.trade_list.extend(self.trades)
        self.trade_list.append(self.trades[0])
        self.trade_list[0] = self.trades[1]

    def test_special_methods_validation(self):
        with self.assertRaises(ValueError):
            self.trade_list += self.random_list
        with self.assertRaises(ValueError):
            self.trade_list = self.trade_list + self.random_list
        with self.assertRaises(ValueError):
            self.trade_list.extend(self.random_list)
        with self.assertRaises(ValueError):
            self.trade_list.append(self.random_list[0])
        with self.assertRaises(ValueError):
            self.trade_list[0] = self.random_list[1]

if __name__ == '__main__':
    unittest.main()
