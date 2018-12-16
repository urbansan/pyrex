import os
import sys
import unittest
from datetime import datetime as dt, timedelta as td
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


from pyrex._tests.test_validators import *
from pyrex._tests.test_contracts import *
from pyrex._tests.test_trades import *
from pyrex._tests.test_status_flows import *


if __name__ == '__main__':
    unittest.main()