from functools import wraps


def deco_moreno(cls):
    for name, attr in cls.__dict__.items():
        # print(f'siusiaki {name}, {attr}')
        if not callable(attr) or name.startswith('_'):
            print(f'not callable {name}, {attr}')
        else:
            print(f'callable {name}, {attr}')

            wraps(attr)
            def dupa(self, *args):
                print('kutaski')
                return self.attr(*args)
            # dupa.__name__ = name
            # self.
            cls.__dict__[name] = dupa
        #     print(f'modified functions {name}, {attr}')

        #     def wrapper(self, *args, **kwargs):
        #         print(f'Print inner attr {name}')
        #         ret_val = attr(self, *args, **kwargs)
        #         if not all(isinstance(obj, int) for obj in self.data):
        #             raise ValueError('Contract elements should all be Trade instances')
        #         return ret_val
        #     wrapper.__set_name = name
            
    return cls

# @deco_moreno
# class A:
#     def __init__(self):
#         self.data = []
#     def add(self, obj):
#         self.data.append(obj)

def deco(cls):
    class Wrapper:
        def __init__(self, *args):
            self.wrapped = cls(*args)

        def __getattr__(self, name):
            print('Getting the {} of {}'.format(name, self.wrapped))
            ret = getattr(self.wrapped, name)
            if not all(isinstance(obj, str) for obj in self.wrapped.data):
                raise ValueError('Contract elements should all be Trade instances')
            return ret
    return Wrapper

# A = deco(A)
@deco
class A:
    def __init__(self):
        self.data = []
    def add(self, obj):
        self.data.append(obj)

a = A()
print(a.__class__.__dict__)
a.add(1)
# a.add('1')
# a.extend([1, 2])
print(a.data)