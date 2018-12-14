import sys
import os
sys.path.append(os.getcwd())
from .validators import Typology, Numeric, Integer
import collections
import functools

# TODO: what should a base trade class do:
 # - have a db handler: how to interact with a datamodel - maybe by a descriptor?
 # - have methods for PnL calculation
 # - have a flex interface


class Trade:
    _counter = iter(range(999999999))

    def __init__(self, typology, rate, nominal):
        self.typology = Typology(typology)
        self.rate = Numeric(rate)
        self.nominal = Numeric(nominal)
        self.nb = Integer(next(self.__class__._counter))

    def __repr__(self):
        return f"<Trade('{self.typology}', '{self.rate}', '{self.nominal}): {self.nb}>"

    def __str__(self):
        return self.__repr__()


class TradeList(collections.UserList):
    def __getattribute__(self, name):
        data = super().__getattribute__('data')
        if not all(isinstance(obj, Trade) for obj in data):
            raise ValueError('Contract elements should all be Trade instances')
        return super().__getattribute__(name)

    def __setattr__(self, name, val):
        super().__setattr__(name, val)
        data = super().__getattribute__('data')
        if not all(isinstance(obj, Trade) for obj in data):
            raise ValueError('Contract elements should all be Trade instances')


class Contract:
    _counter = iter(range(999999999))

    def __init__(self, cnt_typology):
        self.cnt_nb = Integer(next(self.__class__._counter))

    def __repr__(self):
        return f"<Contract('{self.cnt_typology}): {self.cnt_.nb}>"

    def __str__(self):
        return self.__repr__()