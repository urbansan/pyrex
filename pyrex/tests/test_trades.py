import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '../..'))
from pyrex import Trade


class TestTradeInitialization(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_typology_not_in_list(self):
        with self.assertRaises(ValueError):
            Trade('hadouken', rate=0.1, nominal=10_100_999)

    def test_spot_init(self):
        Trade('spot', rate=0.1, nominal=10_100_999)

    def test_spot_bad_init(self):
        with self.assertRaises(ValueError):
            Trade('spot', rate='0.1', nominal='10000')

        with self.assertRaises(TypeError):
            Trade('spot', rate=0.1)

        with self.assertRaises(TypeError):
            Trade('spot', nominal=10000)

    def test_outright(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
