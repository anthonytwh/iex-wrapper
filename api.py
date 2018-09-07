"""

IEX Exchange API Wrapper

Github: anthonytwh

"""

__author__ = 'anthonytwh'
__version__ = 0.1

from .iexbase import _IEXv1
from .stock import Stocks
from .market import Market
from .refdata import RefData
from .stats import Stats
from .deep import Deep
from .tops import Tops


_IEXBASE = "https://api.iextrading.com/1.0/"

def testing():
	return print('testing works')

class IEXv1():
	def __init__(self, param1): # list intake params
		self.help = []
		print ("IEXv1", param1)
		pass

	def _request(self):
		# run request of params
		pass


def stock(symbol, method, params=None, **kwargs):

	_methods = ['book', 'chart', 'company', 
				'delayed-quote', 'dividends', 'earnings', 
				'effective-spread', 'financials', 'stats', 
				'largest-trades', 'logo', 'news', 
				'ohlc', 'peers', 'previous', 
				'price', 'quote', 'relevant', 
				'splits', 'time-series', 'volume-by-venue']

	if not(isinstance(symbol, str)):
		raise TypeError("Input symbol must be type String.")
	if not any(method in query for query in _methods):
		raise ValueError("Endpoint query unavailble in the API.")
	return Stocks(symbol, method, params, **kwargs)

def market(method, params, **kwargs): # run params through market.py 
	# +Batch case
	pass

def refdata(method, params, **kwargs): # run params through refdata.py 
	pass

def stats(method, params, **kwargs): # run params through stats.py 
	pass

def deep(method, params, **kwargs): # run params through deep.py
	pass

def tops(method, params, **kwargs): # run params through tops.py 
	pass



