"""

IEX Exchange API Wrapper


"""

__author__ = 'anthonytwh'
__version__ = 0.1

import requests
from .iexbase import _IEXv1

'''
TODO:

- handle list input

- check query

- check data return


'''


class Stocks(_IEXv1):
	"""
	Pull stock related data from IEX Exchange API

	Object Outputs
	--------------
	.type
	-----
		- returns data type 

	.symbol
	-------
		- returns input query symbol

	.method
	-------
		- returns endpoint method called

	.params
	-------
		- returns input params

	.json
	------
		- returns raw data

	"""
	def __init__(self, symbol, method, params, **kwargs):
		self.type = 'stock'
		self.symbol = symbol
		self.method = method
		if params == None:
			self._query_noparams(symbol, method, **kwargs)
		else:
			self.params = params
			self._query_params(symbol, method, params, **kwargs)
		self._run_query(self.query)

	def _query_noparams(self, symbol, method, **kwargs):
		self.query = '{u}/{t}/{s}/{m}'.format(
			u=self._BASE_URL, 
			t=self.type,
			s=symbol,
			m=method)

	def _query_params(self, symbol, method, params, **kwargs):
		self.query = '{u}/{t}/{s}/{m}?{p}'.format(
			u=self._BASE_URL, 
			t=self.type,
			s=symbol,
			m=method,
			p=params)

	def _run_query(self, query):
		self.output = requests.get(query).json()
		
