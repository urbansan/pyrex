class Base:
    @classmethod
    def __init__subclass__(cls):
        print('siusiaki lataki')
        for name, attr in cls.__dict__.items():
            
            if callable(attr):
                setattr(cls, name, cls.checked(val))

class Under(Base):
    def dupa(self):
        print('in dupa')


class Now(Under):
    pass

a = Under()
b = Now()