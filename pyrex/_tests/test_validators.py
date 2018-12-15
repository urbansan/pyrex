import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '../..'))
from pyrex import validators


class Dummy:
    typology = validators.Typology('typology')
    numeric = validators.Numeric('numeric')


class TestTradeValidators(unittest.TestCase):

    def setUp(self):
        self.test_object = Dummy()

    def tearDown(self):
        del self.test_object

    def test_Typology(self):
        self.test_object.typology = 'spot'
        self.assertEqual(self.test_object.typology, 'spot')
        self.test_object.typology = 'outright'
        self.assertEqual(self.test_object.typology, 'outright')

    def test_Typology_raises(self):
        with self.assertRaises(ValueError):
            self.test_object.typology = 'hadouken'

    def test_Numeric(self):
        self.test_object.numeric = 10
        self.assertEqual(self.test_object.numeric, 10.)
        self.test_object.numeric = 10.10
        self.assertEqual(self.test_object.numeric, 10.1)
        self.test_object.numeric = '10'
        self.assertEqual(self.test_object.numeric, 10.)
        self.test_object.numeric = '10.10'
        self.assertEqual(self.test_object.numeric, 10.1)

    def test_Numeric_raises(self):
        with self.assertRaises(ValueError):
            self.test_object.numeric = 'siemano'

    def test_double_dummy(self):
        new_obj = Dummy()
        new_obj.numeric = 10
        self.test_object.numeric = 20
        self.assertEqual(new_obj.numeric, 10)
        self.assertEqual(self.test_object.numeric, 20)

if __name__ == '__main__':
    unittest.main()
