"""

IEX Exchange API Wrapper


"""
import requests

from .iexbase import _IEXv1

'''
TODO:

- handle list input

- deal with kwargs

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
		self.symbol = symbol
		self.method = method
		self.params = params
		self._check_params(**kwargs)
		self._run_query(self.query)

	def _check_params(self, **kwargs):
		if self.params == None:
			self._query_noparams(self.symbol, self.method, **kwargs)
		if not (self.method == None or '') and not(self.params == None):
			self._query_params(self.symbol, self.method, self.params, **kwargs)

	@property
	def type(self):
		return str('stock')

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

	def _run_batch(self): # Batch query of multiple stocks
		pass



		
