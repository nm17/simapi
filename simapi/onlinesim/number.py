import simapi.api_handler as baseapi


class OnlineSMSNumber(baseapi.Number):
    def __init__(self, api_handler, *args, **kwargs):
        self.__api_handler = api_handler
        super().__init__(*args, **kwargs)

    async def set_activation_status(self, status: int):
        pass

    @property
    async def activation_code(self):
        pass