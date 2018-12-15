import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from datetime import datetime as dt, timedelta as td

from pyrex import Trade, Contract, typologies
from pyrex.classes.contract import TradeList

class TestTypologies(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fx_swap_init(self):
        fx1 = typologies.fx_swap('eur', 4800, 'pln', 1000, dt.now() + td(days=1))
        self.assertEqual(len(fx1.trades), 2)
        self.assertEqual(fx1.trades[0].typology, 'spot')
        self.assertEqual(fx1.trades[1].typology, 'spot')

        fx1 = typologies.fx_swap('eur', 4800, 'pln', 1000, dt.now() + td(days=2))
        self.assertEqual(len(fx1.trades), 2)
        self.assertEqual(fx1.trades[0].typology, 'spot')
        self.assertEqual(fx1.trades[1].typology, 'spot')

        fx1 = typologies.fx_swap('eur', 4800, 'pln', 1000, dt.now() + td(days=20))
        self.assertEqual(len(fx1.trades), 2)
        self.assertEqual(fx1.trades[0].typology, 'spot')
        self.assertEqual(fx1.trades[1].typology, 'outright')

        fx1 = typologies.fx_swap('eur', 4800, 'pln', 1000,
                                 dt.now() + td(days=20),
                                 delayed_start=dt.now() + td(days=10))
        self.assertEqual(len(fx1.trades), 2)
        self.assertEqual(fx1.trades[0].typology, 'outright')
        self.assertEqual(fx1.trades[1].typology, 'outright')


if __name__ == '__main__':
    unittest.main()