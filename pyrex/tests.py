import os
import sys
import unittest
from datetime import datetime as dt, timedelta as td
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


# from pyrex._tests import *
from pyrex._tests.test_contracts import *
from pyrex._tests.test_typologies import *
from pyrex._tests.test_status_flows import *
from pyrex._tests.test_validators import *
# from pyrex import Trade, Contract, typologies
# from pyrex.classes.contract import TradeList

if __name__ == '__main__':
	unittest.main()