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


class BaseContract:
    """For Validation of elements to be type Trade"""
    def __init__(self, *args):
        print('init in BaseContract')
        super().__init__(*args)

    @staticmethod
    def checked(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            ret_val = func(self, *args, **kwargs)
            if not all(isinstance(obj, Trade) for obj in self.data):
                raise ValueError('Contract elements should all be Trade instances')
            return ret_val
        return wrapper

    @classmethod
    def __init__subclass__(cls):
        print('siusiaki lataki')
        for name, attr in cls.__dict__.items():
            
            if callable(attr):
                setattr(cls, name, cls.checked(val))


class Contract(BaseContract, collections.UserList):
    def __init__(self, *args):
        super().__init__(*args)


    def __setitem__(self, key, item):
        if isinstance(item, Trade):
            super().__setitem__(key, item)
        else:
            raise ValueError('Can append only Trade instance')

    def append(self, item):
        if isinstance(item, Trade):
            super().append(item)
        else:
            raise ValueError('Can append only Trade instance')

    def extend(self, items: list):
        if all([isinstance(item, Trade) for item in items]):
            super().extend(items)
        else:
            raise ValueError('Can append only Trade instance')




