"""

IEX Exchange API Wrapper

Github: anthonytwh

"""

__author__ = 'anthonytwh'
__version__ = 0.1

import requests

from .stock import Stocks
from .market import Market
from .refdata import RefData
from .stats import Stats
from .deep import Deep
from .tops import Tops


_IEXBASE = "https://api.iextrading.com/1.0/"

class IEX_v1():
	def __init__(self): # list intake params
		# list vars
		pass

	def request(self):
		# run request of params
		pass


def stock(symb, method, params, **kwargs): # run params through stocks.py 
	# +Batch case
	pass

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



