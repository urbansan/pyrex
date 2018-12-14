from collections import UserList

# def check(self):
#     if not all(isinstance(obj, Trade) for obj in self.wrapped.data):
#         raise ValueError('Contract elements should all be Trade instances')
class lizd(UserList):
    def __init_(self, *args):
        super().__init__(*args)
        # self._data = super().data
        # self.data = TradeInstance(self.data)

    def __getattribute__(self, name):
        # print('in getattribute', name)
        data = super().__getattribute__('data')
        if not all(isinstance(obj, int) for obj in data):
            raise ValueError('Contract elements should all be Trade instances')
        return super().__getattribute__(name)

    # def __setattribute__(self, name, val):
    #     print('__setattribute__')
    #     data = super().__getattribute__('data')
    #     if not all(isinstance(obj, str) for obj in data):
    #         raise ValueError('Contract elements should all be Trade instances')
    #     super().__setattribute__(name, val)
    # def __getattr__(self, name):
    #     print('in getattr', name)


l = lizd()
from inspect import signature
print(signature(l.__setattr__))
print(dir(l))

# l.append(1)
print(l)

l += [1, 2]
l = l + l

print(l)