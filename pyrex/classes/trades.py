import sys
import os
import collections
from .validators import Typology, Numeric, Integer, Currency, Date
from datetime import datetime as dt, date, timedelta as td
from abc import ABCMeta, abstractmethod

class Trade(metaclass=ABCMeta):
    _counter = iter(range(100000000, 999999999))
    nb = Integer()

    def __init__(self):
        self.nb = next(type(self)._counter)

    def __repr__(self):
        return f"<Trade('{type(self).__name__}': {self.nb}>"

    def __str__(self):
        return self.__repr__()

    # @classmethod
    # @abstractmethod
    # def from_factory_kwargs(cls, **kwargs):
    #     pass

    @abstractmethod
    def rate(self):
        pass


class typologies:
    class Spot(Trade):
        currency1 = Currency()
        nominal1 = Numeric()
        currency2 = Currency()
        nominal2 = Numeric()
        start = Date()
        maturity = Date()

        def __init__(self, currency1, currency2, nominal1, nominal2, start=date.today()):
            super().__init__()
            self.currency1 = currency1
            self.nominal1 = nominal1
            self.currency2 = currency2
            self.nominal2 = nominal2
            self.start = start
            self.maturity = start + td(days=2)

        def rate(self):
            return self.nominal2 / self.nominal1


    class Outright(Trade):
        currency1 = Currency()
        nominal1 = Numeric()
        currency2 = Currency()
        nominal2 = Numeric()
        start = Date()
        maturity = Date()

        def __init__(self, currency1, currency2, nominal1, nominal2, start, maturity):
            super().__init__()
            self.currency1 = currency1
            self.nominal1 = nominal1
            self.currency2 = currency2
            self.nominal2 = nominal2
            self.start = start
            self.maturity = maturity


        def rate(self):
            return self.nominal2 / self.nominal1

def get_trade(
        typology,
        currency1=None,
        currency2=None,
        nominal1=None,
        nominal2=None,
        start=date.today(),
        maturity=None,
        rate = None):
    """Trade factory"""


    if typology.lower() == 'spot':
        return typologies.Spot(currency1, currency2, nominal1, nominal2, start)
    elif typology.lower() == 'outright' \
            and isinstance(maturity, date) \
            and maturity - start <= td(days=2):
        return typologies.Spot(currency1, currency2, nominal1, nominal2, start)
    elif typology.lower() == 'outright':
        return typologies.Outright(currency1, currency2, nominal1, nominal2, start, maturity)
    else:
        raise ValueError(f'Typology {typology} does not exist or argument conditions are invalid')


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

