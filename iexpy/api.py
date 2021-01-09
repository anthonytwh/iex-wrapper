"""
Wrapper functions

"""

import iexpy.endpoints as ep

from iexpy.core.stocks import Stock
from iexpy.core.markets import Market
from iexpy.core.refdata import RefData
from iexpy.core.stats import Stats
from iexpy.core.deep import Deep
from iexpy.core.tops import Tops

print (ep.core_data)

def stock(symbol, method, params=None, **kwargs):
    _methods = ['book', 'chart', 'company', 
                'delayed-quote', 'dividends', 'earnings', 
                'effective-spread', 'financials', 'stats', 
                'largest-trades', 'logo', 'news', 
                'ohlc', 'peers', 'previous', 
                'price', 'quote', 'relevant', 
                'splits', 'time-series', 'volume-by-venue']

    if method == None or '':
        raise ValueError("Method input is required for stock queries.")
    if not(isinstance(symbol, str)):
        raise TypeError("Input symbol must be type String.")
    if not any(method in query for query in _methods):
        raise ValueError("Endpoint query unavailble in the API.")
    return Stock(symbol, method, params, **kwargs)

def market(method, params=None, **kwargs):
    """
    
    """
    _methods = ['', 'batch', 'collection', 
                'crypto', 'list', 'news',
                'ohlc','previous','sector-performance', 
                'short-interest','threshold-securities', 'today-earnings',
                'today-ipos', 'upcoming-ipos']

    if not any(method in query for query in _methods):
        raise ValueError("Endpoint query unavailble in the API.")
    return Market(method, params, **kwargs)

def refdata(method, params, **kwargs): # run params through refdata.py 
    pass

def stats(method, params, **kwargs): # run params through stats.py 
    pass

def deep(method, params, **kwargs): # run params through deep.py
    pass

def tops(method, params, **kwargs): # run params through tops.py 
    pass

