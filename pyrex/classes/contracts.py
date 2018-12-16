import sys
import os
from .validators import Typology, Numeric, Integer, ContractTypology
from .trades import TradeList, TradeFactory
import collections
import functools
import abc



class Contract(metaclass=abc.ABCMeta):
    _counter = iter(range(100000000, 999999999))
    nb = Integer('cnt_nb')
    typology = ContractTypology('typology')

    def __init__(self):
        self.typology = self.__class__.__name__
        self.nb = next(self.__class__._counter)
        self.trades = TradeList()

    def __repr__(self):
        return f"<Contract('{self.cnt_typology}): {self.cnt_.nb}>"

    def __str__(self):
        return self.__repr__()

    @abc.abstractmethod
    def pnl(self):
        pass


class contract_typologies:
    class Spot:
        def __init__(self, typology, currency1, nominal1, currency2, nominal2):
            t = TradeFactory(typology, currency1, nominal1, currency2, nominal2)
            self.trades.append(t)

        def pnl(self):
            return licz cos :)

class ContractFactory:
    pass