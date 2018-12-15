import collections


class Typology:
    _typology_list = [
        'spot',
        'outright'
    ]

    def __init__(self, name=None):
        self.__set__('', name)

    def __set__(self, obj, value):

        if isinstance(value, str) and value in self._typology_list:
            self._name = value
            return value
        else:
            raise ValueError('Incorrect typology')

    def __get__(self, obj, value=None):
        return self._name

    def __repr__(self):
        return f'{self._name}'

    def __str__(self):
        return self.__repr__()

class Numeric:
    def __init__(self, initial_value=0):
        self._value = float(initial_value)

    def __set__(self, obj, value):
        self._value = float(value)

    def __get__(self, obj, value=None):
        return self._value

    def __repr__(self):
        return f'{self._value}'

    def __str__(self):
        return self.__repr__()


class Integer:
    def __init__(self, initial_value=0):
        self._value = int(initial_value)

    def __set__(self, obj, value):
        self._value = int(value)

    def __get__(self, obj, value=None):
        return self._value

    def __repr__(self):
        return f'{self._value}'

    def __str__(self):
        return self.__repr__()

