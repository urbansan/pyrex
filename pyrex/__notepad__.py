from classes.contract import Contract, Trade, TradeList

t = TradeList(static_type=int)

t.append(1)
t.append('dupa')
print(t.data)