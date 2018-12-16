import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from pyrex.classes.trades import TradeFactory, typologies, TradeList
from datetime import datetime as dt, timedelta as td


class TestTradeFactory(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_typology_not_in_list(self):
        with self.assertRaises(ValueError):
            TradeFactory('hadouken', 'eur', rate=0.1, nominal=10_100_999)

    def test_spot_init(self):
        t1 = TradeFactory('spot', currency='eur', rate=0.1, nominal=10_100_999)
        self.assertIsInstance(t1, typologies.Spot)
        t2 = TradeFactory('spot', currency='eur', rate='0.1', nominal='10000')
        self.assertIsInstance(t2, typologies.Spot)
        t3 = TradeFactory('spot', currency='eur', rate=0.1, nominal='10000.0')
        self.assertIsInstance(t3, typologies.Spot)
        with self.assertRaises(ValueError):
            TradeFactory('spot', currency='eur', rate='random_string', nominal='10000.0')

    def test_outright_init(self):
        maturity =  dt.now() + td(days=7)
        t1 = TradeFactory('outright', currency='eur', rate=0.1, nominal=10_100_999, maturity=maturity)
        self.assertIsInstance(t1, typologies.Outright)
        t2 = TradeFactory('outright', currency='eur', rate='0.1', nominal='10000', maturity=maturity)
        self.assertIsInstance(t2, typologies.Outright)
        t3 = TradeFactory('outright', currency='eur', rate=0.1, nominal='10000.0', maturity=maturity)
        self.assertIsInstance(t3, typologies.Outright)
        with self.assertRaises(ValueError):
            TradeFactory('outright', currency='eur', rate='random_string', nominal='10000.0', maturity=maturity)


class TestTradeList(unittest.TestCase):
    def setUp(self):
        self.trades = [
            TradeFactory('spot', 'eur', 10, 20),
            TradeFactory('spot', 'eur', 20, 10),
            TradeFactory('outright', 'eur', 11, 10)
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

