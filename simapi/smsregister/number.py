from simapi.number import Number
import simapi.smsregister.exceptions as simexp


class SMSRegNumber(Number):
    def __init__(self, api_handler, *args, **kwargs):
        self.__api_handler = api_handler
        super().__init__(*args, **kwargs)

    @property
    async def activation_code(self):
        resp = await self.__api_handler.send_request('')
        try:
            status, code = resp.split(':')
        except ValueError:
            raise simexp.CodeNotReceivedYetException()
        if status != 'STATUS_OK':
            raise simexp.CodeNotReceivedYetException()
        return code

    async def set_activation_status(self, status: int):
        resp = self.__api_handler.send_request('setStatus',
                                               id=self.id,
                                               status=status,
                                               forward=self.forward)
        exc = simexp.exception_status_dict.get(resp, None)
        if exc is not None:
            raise exc()
