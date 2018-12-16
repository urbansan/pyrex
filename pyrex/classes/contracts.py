import sys
import os
from .validators import Typology, Numeric, Integer
from .trades import TradeList
import collections
import functools

# TODO: what should a base trade class do:
 # - have a db handler: how to interact with a datamodel - maybe by a descriptor?
 # - have methods for PnL calculation
 # - have a flex interface



class Contract:
    _counter = iter(range(100000000, 999999999))
    cnt_nb = Integer('cnt_nb')

    def __init__(self, cnt_typology):
        self.cnt_nb = next(self.__class__._counter)
        self.trades = TradeList()

    def __repr__(self):
        return f"<Contract('{self.cnt_typology}): {self.cnt_.nb}>"

    def __str__(self):
        return self.__repr__()

class cnt_typologies:
    pass

class ContractFactory:
    pass