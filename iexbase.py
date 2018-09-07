"""

IEX Exchange API Wrapper

Github: anthonytwh

"""

__author__ = 'anthonytwh'
__version__ = 0.1

import requests

class _IEXv1():
	def __init__(self, param1): # list intake params
		self.help = []
		print ("IEXv1", param1)
		pass

	def _request(self, input):
		# run request of params
		print ("IEXv1 _request", input)
		pass

def testing():
	return print('testing works')