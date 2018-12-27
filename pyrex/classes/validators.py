"""Validators based on Descriptor protocol"""
from abc import ABCMeta, abstractmethod


class BaseValidator(metaclass=ABCMeta):
    def __set_name__(self, owner, name):
        self.property_name = f'_{type(self).__name__}_{name}'

    def __set__(self, instance, value):
        checked_value = self.check(value)
        setattr(instance, self.property_name, checked_value)

    def __get__(self, instance, owner):
        return getattr(instance, self.property_name)

    def __repr__(self):
        return f'{type(self).__name__}() field'

    @abstractmethod
    def check(self, value):
        """Tries to check and convert types if possible. In other casses should throw and exception"""
        return value


class Typology(BaseValidator):
    _typology_list = [
        'spot',
        'outright']

    def check(self, value):
        if isinstance(value, str) and value in self._typology_list:
            return value
        else:
            raise ValueError('Incorrect typology')


class ContractTypology(BaseValidator):
    _typology_list = [
        'spot',
        'outright',
        'fx_swap']

    def check(self, value):
        if isinstance(value, str) and value in self._typology_list:
            return value
        else:
            raise ValueError('Incorrect typology')


class Numeric(BaseValidator):
    def check(self, value):
        return float(value)


class Integer(BaseValidator):
    def check(self, value):
        return int(value)


class Date(BaseValidator):
    def check(self, value):
        from datetime import date
        if isinstance(value, date):
            return value
        else:
            raise ValueError('Date field required a Datetime.Date type')


class Currency(BaseValidator):
    _currencies = [
        'eur',
        'usd',
        'pln']

    def check(self, value):
        if isinstance(value, str) and value in self._currencies:
            return value
        else:
            raise ValueError(f'Currency abbreviation not recognized: {str(value)}')
