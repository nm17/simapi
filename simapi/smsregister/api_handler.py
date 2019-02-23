import json
from typing import Optional

import simapi.smsregister.exceptions as simexp
import simapi.api_handler as baseapi
from simapi.smsregister.number import SMSRegNumber

countries = [  # ISO 3166-1 alpha-3 codes in SMSReg specific order TODO
    'RUS',
    'UKR',
    'KAZ',
    'CHN',
    'PHL',
    'MMR',
    'IDN',
    'MYS',
    'KEN',
    'VNM',
    'KGZ',
    'USA',
    'ISR'
]


class SMSRegAPIHandler(baseapi.ApiHandler):
    def __init__(self, api_key: str, site: str):
        super().__init__(api_key)
        self.site = site
        self.numbers = []

    async def send_request(self, action: str, **kwargs):
        """
        Отправляет реквест на сервер автоматически добавляя
        :param action: Вид действия
        :param kwargs:
        :return: HTTP текст ответа
        """
        with self:
            async with self.session.get('https://{}/stubs/handler_api.php'.format(self.site),
                                        params={'api_key': self._api_key, 'action': action, **kwargs}) as req:
                return await req.text()

    @property
    async def balance(self):
        resp = await self.send_request('getBalance')
        try:
            status, answer = resp.split(':')
        except ValueError:
            raise simexp.exception_status_dict.get(resp, simexp.UnknownStatusException)()

        return float(answer)

    async def request_number(self, country: int, operator: str, forward: bool, service: str):
        with self:
            resp = await self.send_request(
                'getNumber',
                service=service,
                forward=int(forward),
                operator=operator,
                country=country)
            try:
                status, id_, number = resp.split(':')
            except ValueError:
                raise simexp.exception_status_dict.get(resp, simexp.UnknownStatusException)()
            if status == 'ACCESS_NUMBER':
                self.numbers += SMSRegNumber(self, service, id_, number, forward, operator, country)

    async def total_numbers_available(self, country: int, operator: Optional[str] = None):
        req_args = {
            'country': country
        }
        if operator is not None:
            req_args['opearator'] = operator
        resp = await self.send_request('getNumbersStatus', **req_args)
        return json.loads(resp)



