"""
IEX Cloud Base Object

"""
import requests

import time
import os
import logging


class _IEX_Cloud(object):

    _API_VERSION = {
        "stable": "https://cloud.iexapis.com/stable/",
        "latest": "https://cloud.iexapis.com/latest/",
        "beta": "https://cloud.iexapis.com/beta/",
        "sandbox": "https://sandbox.iexapis.com/stable/",
        "iexcloud-beta": "https://cloud.iexapis.com/beta/",
        "iexcloud-v1": "https://cloud.iexapis.com/v1/",
        "iexcloud-sandbox": "https://sandbox.iexapis.com/stable/"
    }

    def __init__(self, **kwargs):
        
        # API Token
        self.api_token = kwargs.get("api_token")
        if self.api_token is None:
            self.api_token = os.getenv("IEX_API_TOKEN")
        if not self.api_token or not isinstance(self.api_token, str):
            raise ValueError( "The IEX Cloud API key must be provided via the 'api_token' variable or as an environmental variable 'IEX_API_TOKEN'.")

        # API Version (default == stable)
        self.api_version = os.getenv("IEX_API_VERSION", "stable")
        if self.api_version not in list(self._API_VERSION.keys()):
            raise ValueError("Please select a valid API version.")

        # Default Version to Sandbox if Sandbox token is detected
        if self.api_token.startswith(("Tsk", "Tpk")):
            logging.logger.info("Using a sandboxed environment because a test key was detected")
            os.environ["IEX_API_VERSION"] = "sandbox"

    def _run_query(self):
        pass

    def _check_Query(self):
        pass

    def _check_Data(self):
        pass