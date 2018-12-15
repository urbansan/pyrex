from datetime import datetime as dt, timedelta as td
from .contract import Contract, Trade

def fx_swap(currency1, nominal1, currency2, nominal2, maturity: dt, delayed_start: dt = None):
    fx_swap = Contract('fx_swap')
    if delayed_start and delayed_start - dt.now() > td(days=2):
    	typo1 = 'outright'
    else:
    	typo1 = 'spot'

    if maturity - dt.now() > td(days=2):
    	typo2 = 'outright'
    else:
    	typo2 = 'spot'
    
    rate = nominal1/nominal2

    fx_swap.append(Trade(typo1, currency1, nominal1, rate))
    fx_swap.append(Trade(typo2, currency2, nominal2, 1/rate))
    return fx_swap