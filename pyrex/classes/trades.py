import sys
import os
import collections
from .validators import Typology, Numeric, Integer, Currency, Date
from datetime import datetime as dt, date, timedelta as td
import abc

class Trade(metaclass=abc.ABCMeta):
    _counter = iter(range(100000000, 999999999))
    typology = Typology('typology')
    nb = Integer('nb')

    def __init__(self):
        self.typology = self.__class__.__name__
        self.nb = next(self.__class__._counter)

    def __repr__(self):
        return f"<Trade('{self.typology}': {self.nb}>"

    def __str__(self):
        return self.__repr__()

    @abc.abstractmethod
    def rate(self):
        pass


class typologies:
    class Spot(Trade):
        currency1 = Currency('currency1')
        nominal1 = Numeric('nominal1')
        currency2 = Currency('currency1')
        nominal2 = Numeric('nominal2')
        maturity = Date('maturity')

        def __init__(self, currency1, nominal1, currency2, nominal2):
            super().__init__()
            self.currency1 = currency1
            self.nominal1 = nominal1
            self.currency2 = currency2
            self.nominal2 = nominal2
            self.maturity = date.today() + td(days=2)

        def rate(self):
            return self.nominal2 / self.nominal1


    class Outright(Trade):
        currency1 = Currency('currency1')
        nominal1 = Numeric('nominal1')
        currency2 = Currency('currency1')
        nominal2 = Numeric('nominal2')
        maturity = Date('maturity')

        def __init__(self, currency1, nominal1, currency2, nominal2, maturity):
            super().__init__()
            self.currency1 = currency1
            self.nominal1 = nominal1
            self.currency2 = currency2
            self.nominal2 = nominal2
            self.maturity = maturity

        def rate(self):
            return self.nominal2 / self.nominal1


def TradeFactory(typology, currency1, nominal1, currency2, nominal2, maturity=date.today()):
    if typology.lower() == 'spot':
        return typologies.Spot(currency1, nominal1, currency2, nominal2)
    if typology.lower() == 'outright':
        return typologies.Outright(currency1, nominal1, currency2, nominal2, maturity)
    else:
        raise ValueError(f'Typology {typology} does not exist')


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

