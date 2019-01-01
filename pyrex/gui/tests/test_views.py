import unittest
from .. import views


class WebappTest(unittest.TestCase):
    def test_index(self):
        a = views.index()
        print(a)
