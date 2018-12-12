class Typology:
    _typology_list = [
        'spot',
        'outright'
    ]

    def __set__(self, obj, value):
        if isinstance(value, str) and value in self._typology_list:
            self._name = value
            return value
        else:
            raise ValueError('Incorrect typology')

    def __get__(self, obj, value=None):
        return self._name


class Numeric:

    def __set__(self, obj, value):
        if isinstance(value, str) and value in self._typology_list:
            self._name = value
            return value
        else:
            raise ValueError('Incorrect typology')

    def __get__(self, obj, value=None):
        return self._name
