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
        self.nb = Integer()
        self.nb = next(self.__class__._counter)

    def __repr__(self):
        return f"<Trade('{self.typology}', '{self.rate}', '{self.nominal}): {self.nb}>"

    def __str__(self):
        return self.__repr__()


def only_Trade_instances(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def check(self):
            if not all(isinstance(obj, Trade) for obj in self.wrapped.data):
                raise ValueError('Contract elements should all be Trade instances')

        def __getattr__(self, name):
            # print('Getting the {} of {}'.format(name, self.wrapped))
            ret = getattr(self.wrapped, name)
            self.check()
            return ret

        def __iadd__(self, obj):
            self.wrapped.data.__iadd__(obj)
            self.check()
            return self

        def __add__(self, obj):
            new = self.__class__(self.wrapped.data)
            new.wrapped.data = self.wrapped.data.__add__(obj)
            self.check()
            return new

        def __iter__(self):
            return iter(self.wrapped.data)
        # Wrapped.__class__ = cls.__class__
    return Wrapper


# @only_Trade_instances
class Contract(collections.UserList):
    def __getattribute__(self, name):
        # print('in getattribute', name)
        data = super().__getattribute__('data')
        if not all(isinstance(obj, Trade) for obj in data):
            raise ValueError('Contract elements should all be Trade instances')
        return super().__getattribute__(name)

    def __setattr__(self, name, val):
        print('__setattr__')
        super().__setattr__(name, val)
        data = super().__getattribute__('data')
        if not all(isinstance(obj, Trade) for obj in data):
            raise ValueError('Contract elements should all be Trade instances')
        