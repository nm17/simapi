from typing import Optional, Dict

import simapi.api_handler as baseapi
from simapi.number import Number


class OnlineSMSAPIHandler(baseapi.ApiHandler):
    def __init__(self, api_key: Optional[str] = None, *args, **kwargs):
        self.demo = False
        if api_key is None:
            self.demo = True
        super().__init__(*args, **kwargs)

    @property
    async def balance(self) -> float:
        pass

    async def request_number(self, country: int, operator: str, forward: bool, service: str) -> Number:
        pass

    async def total_numbers_available(self, country: int, operator: str) -> Dict:
        pass
