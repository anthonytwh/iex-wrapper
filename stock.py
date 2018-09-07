"""

IEX Exchange API Wrapper

Github: anthonytwh

"""

__author__ = 'anthonytwh'
__version__ = 0.1

import requests

from .iexbase import _IEXv1

_IEXv1("help")

class Stocks(_IEXv1):
	def __init__(self, symbol, method, params, **kwargs):
		print ('made it to stock.py')
		print (symbol, method, params, **kwargs)

		self._request("yolo")
		pass

	def run_query(self):
		pass

	def batch(self): #special case for batch query of 1 stock
		pass

