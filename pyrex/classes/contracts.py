import sys
import os
from datetime import date
from .validators import Typology, Numeric, Integer, ContractTypology
from .trades import TradeList, get_trade
import collections
import functools
import abc



class Contract(metaclass=abc.ABCMeta):
    _counter = iter(range(100000000, 999999999))
    nb = Integer()

    def __init__(self):
        self.nb = next(type(self)._counter)
        self.trades = TradeList()

    def __repr__(self):
        return f"<Contract('{type(self).__name__}): {self.nb}>"

    @abc.abstractmethod
    def pnl(self, market_data):
        pass


class contract_typologies:
    class Spot(Contract):
        def __init__(self, currency1, currency2, nominal1, nominal2, start):
            super().__init__()
            t = get_trade('spot', currency1, currency2, nominal1, nominal2, start)
            self.trades.append(t)
            self.trade = t

        def pnl(self, market_data):
            t = self.trade
            mv_nominal2 = market_data['fx'][t.currency2][t.currency1] * t.nominal1
            return t.nominal1 - mv_nominal2

    class Outright(Contract):
        def __init__(self, currency1, currency2, nominal1, nominal2, start, maturity):
            super().__init__()
            t = get_trade('outright', currency1, currency2, nominal1, nominal2, start, maturity)
            self.trades.append(t)
            self.trade = t

        def pnl(self, market_data):
            t = self.trade
            mv_nominal2 = market_data['fx'][t.currency2][t.currency1] * t.nominal1
            return t.nominal1 - mv_nominal2

    class FxSwap(Contract):
        def __init__(
                self,
                currency1, currency2,
                nominal1, nominal2,
                start,
                maturity1, maturity2):
            super().__init__()
            self.trades.extend([
                get_trade('outright', currency1, currency2, nominal1, nominal2, start, maturity1),  # should get Spot instance if maturity is too short
                get_trade('outright', currency1, currency2, nominal1, nominal2, start=maturity1, maturity=maturity2),
            ])


        def pnl(self, market_data):
            mv_gen = (market_data['fx'][trade.currency2][trade.currency1] for trade in self.trades)
            mv = functools.reduce(lambda x, y: x + y, mv_gen)
            return

def get_contract(
        typology,
        currency1=None,
        currency2=None,
        nominal1=None,
        nominal2=None,
        rate=None,
        start=date.today(),
        maturity1=date.today(),
        maturity2=None):
    """Trade factory"""

    if typology.lower() == 'spot':
        return contract_typologies.Spot(currency1, currency2, nominal1, nominal2, start)
    elif typology.lower() == 'outright':
        return contract_typologies.Outright(currency1, currency2, nominal1, nominal2, start, maturity1)
    elif typology.lower() == 'fx_swap':
        return contract_typologies.FxSwap(currency1, currency2, nominal1, nominal2, start, maturity1, maturity2)
    else:
        raise ValueError(f'Typology {typology} does not exist')