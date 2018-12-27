import os
import sys
import unittest
sys.path.append(os.path.join(os.getcwd(), '../..'))
from pyrex.classes import validators


class Dummy:
    typology = validators.Typology()
    numeric = validators.Numeric()


class TestTradeValidators(unittest.TestCase):

    def setUp(self):
        self.test_object = Dummy()

    def tearDown(self):
        del self.test_object

    def test_property_isolation(self):
        test_object2 = Dummy()
        test_object2.typology = 'spot'
        self.test_object.typology = 'outright'
        self.assertNotEqual(test_object2.typology, self.test_object.typology)
        self.assertEqual(test_object2.typology, 'spot')
        self.assertEqual(self.test_object.typology, 'outright')

        test_object2.numeric = 200.0
        self.test_object.numeric = -20
        self.assertNotEqual(test_object2.numeric, self.test_object.numeric)
        self.assertEqual(test_object2.numeric, 200.0)
        self.assertEqual(self.test_object.numeric, -20)

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


if __name__ == '__main__':
    unittest.main()
