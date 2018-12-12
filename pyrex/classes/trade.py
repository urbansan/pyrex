from .validators import Typology

# TODO: what should a base trade class do:
 # - have a db handler: how to interact with a datamodel - maybe by a descriptor?
 # - have methods for PnL calculation
 # - have a flex interface


class Trade:

    typology = Typology()

    def __init__(self, typology, rate, nominal, flex_lib=None):
        self.typology = typology
        self.flex_lib = flex_lib

    @classmethod
    def load_from_db(self, contract_number):
        pass


class Contract:
    pass


if __name__ == '__main__':
    t1 = Trade('spot', 0.1, 1000)
    print(t1.typology)
    t1 = Trade('spot', 0.1)
