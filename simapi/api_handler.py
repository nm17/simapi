import abc
from typing import Dict

import aiohttp

from simapi.number import Number


class ApiHandler(abc.ABC):
    def __init__(self, api_key):
        self._api_key = api_key
        self.__session = None

    @property
    def session(self):
        if self.__session is None:
            self.__session = aiohttp.ClientSession()
        return self.__session

    @property
    @abc.abstractmethod
    async def balance(self) -> float:
        """Get current balance of an account"""
        pass

    @abc.abstractmethod
    async def request_number(self, country: int, operator: str, forward: bool, service: str) -> Number:
        pass

    @abc.abstractmethod
    async def total_numbers_available(self, country: int, operator: str) -> Dict:
        pass

    def __enter__(self):
        """Should be used to automatically close ClientSession"""
        self.__session = aiohttp.ClientSession()

    def __exit__(self, exc_type, exc_value, traceback):
        self.__session.close()
