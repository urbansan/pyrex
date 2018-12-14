from classes.contract import Contract, Trade

c = Contract()
# print(dir(c))
t = Trade('spot', 1, 1)
c.extend([t, t])
# c.__iadd__([t, t])

c = c + [t, t]
print(c.data)
