"""

IEX Exchange API Wrapper


"""
import requests

from .iexbase import _IEXv1

class Market(_IEXv1):
	def __init__(self, method, params, **kwargs):
		self.method = method
		self.params = params
		self._check_params(**kwargs)
		self._run_query(self.query)

	def _check_params(self, **kwargs):
		if (self.method == '' or None):
			return self._query_nomethod(**kwargs)
		if (self.params == None) and not(self.method == '' or None):
			return self._query_noparams(self.method, **kwargs)
		if not (self.params == None and self.method == '' or None):
			return self._query_params(self.method, self.params, **kwargs)

	@property
	def type(self):
		return str('market')

	def _query_nomethod(self, **kwargs):
		self.query = '{u}/{t}'.format(
			u=self._BASE_URL, 
			t=self.type)

	def _query_noparams(self, method, **kwargs):
		self.query = '{u}/{t}/{m}'.format(
			u=self._BASE_URL, 
			t=self.type,
			m=method)

	def _query_params(self, method, params, **kwargs):
		self.query = '{u}/{t}/{m}?{p}'.format(
			u=self._BASE_URL, 
			t=self.type,
			m=method,
			p=params)

	def _run_query(self, query):
		self.output = requests.get(query).json()

	def _run_batch(self): # Batch query of multiple stocks
		pass

