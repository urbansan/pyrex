import collections


class BaseDescriptor:
    def __init__(self, name):
        self.name = name + '__'

    def __get__(self, instance, class_):
        return getattr(instance, self.name)

    def __str__(self):
        return self.__repr__()


class Typology(BaseDescriptor):
    _typology_list = [
        'spot',
        'outright'
    ]

    def __set__(self, instance, value):
        if isinstance(value, str) and value in self._typology_list:
            setattr(instance, self.name, value)
        else:
            raise ValueError('Incorrect typology')

    def __repr__(self):
        return 'Typology() field'


class Numeric(BaseDescriptor):
    def __set__(self, instance, value):
        setattr(instance, self.name, float(value))

    def __repr__(self):
        return 'Numeric() field'


class Integer(BaseDescriptor):
    def __set__(self, instance, value):
        setattr(instance, self.name, int(value))

    def __repr__(self):
        return 'Integer() field'
