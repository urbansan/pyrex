class val_desc:
    def __init__(self, name):
        self.name = name + '__'

    def __set__(self, instance, value):
        print(f'writing to {self.name}')
        setattr(inst, self.name, val)

    def __get__(self, instance, class_):
        print(parent, owner)
        return getattr(parent, self.name)
        

class A:
    val = val_desc('val')


a = A()
# print(dir(A))
a.val = 'wartosc'
# print(dir(a.val))

# a.val = 'wartosc2'
# print(a.val.append(150))
print(a.val, str(a))

b = A()
b.val = 'cos innego'
print(b.val, str(b))