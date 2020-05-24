"""

IEX Exchange API Wrapper


"""

__author__ = 'anthonytwh'
__version__ = 0.1

import requests

class _IEXv1():

	_BASE_URL = "https://api.iextrading.com/1.0"

	def __init__(self):
		# Check HTTP 200
		if not (requests.head(_BASE_URL+'/market').status_code == 200):
			raise ConnectionError("Unable to connect to IEX API at" + _BASE_URL)

	def _Check_Query(self): # function for checking query result
		pass

	def _Check_Data(self):
		pass