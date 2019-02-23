class NoNumbersException(Exception):
    pass


class SQLException(Exception):
    pass


class BadActionException(Exception):
    pass


class NoBalanceException(Exception):
    pass


class BannedException(Exception):
    pass


class UnknownCountryException(Exception):
    pass


class NotRequestedException(Exception):
    pass


class BadKeyException(Exception):
    pass


class AlreadyRequestedException(Exception):
    pass


class UnknownStatusException(Exception):
    pass


class CodeNotReceivedYetException(Exception):
    pass


class BadServiceException(Exception):
    pass


class BadStatusException(Exception):
    pass


class BadActivationException(Exception):
    pass


exception_status_dict = {
    'BAD_KEY': BadKeyException,
    'ERROR_SQL': SQLException,
    'BAD_SERVICE': BadActionException,
    'BAD_STATUS': BadStatusException,
    'BAD_ACTION': BadActionException,
    'NO_ACTIVATION': BadActivationException
}
