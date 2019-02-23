import asyncio

import simapi.smsregister as smsreg


async def main():
    api = smsreg.SMSRegAPIHandler('1c85902330A70617849eb7e8f6be2f78', 'sms-activate.ru')
    print(await api.total_numbers_available(0))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())