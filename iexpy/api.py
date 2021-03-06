"""

IEX Exchange API Wrapper


"""

__author__ = 'anthonytwh'
__version__ = 0.1

from .stock import Stocks
from .market import Market
from .refdata import RefData
from .stats import Stats
from .deep import Deep
from .tops import Tops


def stock(symbol, method, params=None, **kwargs):
	"""
	Stock Endpoints of IEX Exchange API

	Available Endpoints:
	-------------------
		'book':
		------

		'chart':
		-------
			- works well with Pandas DataFrame

		'company':
		---------

		'delayed-quote':
		---------------

		'dividends':
		-----------

		'earnings':
		----------

		'effective-spread':
		------------------

		'financials':
		------------

		'largest-trades':
		----------------

		'logo':
		------

		'news':
		------

		'ohlc':
		------

		'peers':
		-------

		'previous':
		----------
		
		'price':
		-------

		'quote':
		-------

		'relevant':
		----------

		'splits':
		--------

		'stats':
		-------

		'time-series':
		-------------
		
		'volume-by-venue':
		-----------------


	"""
	_methods = ['book', 'chart', 'company', 
				'delayed-quote', 'dividends', 'earnings', 
				'effective-spread', 'financials', 'stats', 
				'largest-trades', 'logo', 'news', 
				'ohlc', 'peers', 'previous', 
				'price', 'quote', 'relevant', 
				'splits', 'time-series', 'volume-by-venue']

	if method == None or '':
		raise InputError("Method input is required for stock queries.")
	if not(isinstance(symbol, str)):
		raise TypeError("Input symbol must be type String.")
	if not any(method in query for query in _methods):
		raise ValueError("Endpoint query unavailble in the API.")
	return Stocks(symbol, method, params, **kwargs)

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



