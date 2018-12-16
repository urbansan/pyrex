import sys
import os
import collections
from .validators import Typology, Numeric, Integer

class Trade:
    _counter = iter(range(100000000, 999999999))
    typology = Typology('typology')
    rate = Numeric('rate')
    nominal = Numeric('nominal')
    nb = Integer('nb')

    def __init__(self, typology, currency, nominal, rate):
        self.typology = typology
        self.rate = rate
        self.nominal = nominal
        self.nb = next(self.__class__._counter)

    def __repr__(self):
        return f"<Trade('{self.typology}', '{self.rate}', '{self.nominal}): {self.nb}>"

    def __str__(self):
        return self.__repr__()


class typologies:
    pass


class TradeFactory:
    pass


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

