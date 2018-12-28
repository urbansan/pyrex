import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from pyrex.classes.trades import get_trade, typologies, TradeList
from datetime import datetime as dt, timedelta as td


class TestTradeFactory(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_typology_not_in_list(self):
        with self.assertRaises(ValueError):
            get_trade('hadouken', 'eur', 'pln', rate=0.1)

    def test_spot_init(self):
        t1 = get_trade('spot', 'eur', 'pln', 10_100_999, 12310123)
        self.assertIsInstance(t1, typologies.Spot)
        with self.assertRaises(ValueError):
            get_trade('spot', 'eur', 'random_string', '10000.0', 1022314)

    def test_outright_init(self):
        maturity =  dt.now() + td(days=7)
        t1 = get_trade('outright', 'eur', 'pln', 10_100_999, 20_230_21, maturity=maturity)
        self.assertIsInstance(t1, typologies.Outright)
        t2 = get_trade('outright', 'eur', 'pln', '10000', 10_21032, maturity=maturity)
        self.assertIsInstance(t2, typologies.Outright)
        with self.assertRaises(ValueError):
            get_trade('outright', 'eur', 'pln', 10_100_999, 20_230_21, maturity=maturity)


class TestTradeList(unittest.TestCase):
    def setUp(self):
        self.trades = [
            get_trade('spot', 'eur', 'pln', 10, 20),
            get_trade('spot', 'pln', 'eur', 20, 10),
            get_trade('outright', 'eur', 'pln', 11, 10)
        ]
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

