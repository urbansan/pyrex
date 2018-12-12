import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '../..'))
from pyrex import validators

class Dummy:
    typology = validators.Typology()


class TestTypologyValidator(unittest.TestCase):

    def setUp(self):
        self.test_class = Dummy()

    def tearDown(self):
        del self.test_class

    def test_Typology(self):
        self.test_class.typology = 'spot'
        self.test_class.typology = 'outright'

    def test_Typology_raises(self):
        with self.assertRaises(ValueError):
            self.test_class.typology = 'hadouken'

if __name__ == '__main__':
    unittest.main()
