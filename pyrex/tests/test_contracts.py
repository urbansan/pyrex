import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from pyrex import Trade, Contract
from pyrex.classes.contract import TradeList

# print(__file__)

class TestTradeInit(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_typology_not_in_list(self):
        with self.assertRaises(ValueError):
            Trade('hadouken', rate=0.1, nominal=10_100_999)

    def test_spot_init(self):
        Trade('spot', rate=0.1, nominal=10_100_999)
        Trade('spot', rate='0.1', nominal='10000')
        Trade('spot', rate=0.1, nominal='10000.0')
        with self.assertRaises(ValueError):
            Trade('spot', rate='random_string', nominal='10000.0')


class TestTradeList(unittest.TestCase):

    def setUp(self):
        self.trades = [Trade('spot', 10, 20), Trade('spot', 20, 10), Trade('outright', 11, 10)]
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
