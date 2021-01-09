import requests

from iexpy.iex import _IEX_Cloud

'''
TODO:
- handle list input
- deal with kwargs
- check query
- check data return

'''

## WIP ##
class Stock(_IEX_Cloud):

	def __init__(self, symbol, method, params, **kwargs):
		self.symbol = symbol
		self.method = method
		self.params = params
		
		# self._get_data(params, **kwargs)
		# self._run_query(self.query)

	@property
	def type(self):
		return str('stock')

	def _get_data(self):
		# self._check_params(params, kwargs)
		pass

	def _check_params(self, params, **kwargs):
		if self.params == None:
			self._query_noparams(self.symbol, self.method)
		if not (self.method == None or '') and not(self.params == None):
			self._query_params(self.symbol, self.method, self.params)

	def _query_noparams(self, symbol, method):
		return '{u}/{t}/{s}/{m}'.format(
			u=self._BASE_URL, 
			t=self.type,
			s=symbol,
			m=method)

	def _query_params(self, symbol, method, params, **kwargs):
		return  '{u}/{t}/{s}/{m}?{p}'.format(
			u=self._BASE_URL, 
			t=self.type,
			s=symbol,
			m=method,
			p=params)

	def _run_query(self, query):
		return requests.get(query).json()

	def _run_batch(self): # Batch query of multiple stocks
		pass



		
