import abc
from typing import Optional, Hashable


class Number(abc.ABC):
    def __init__(self, service: str, id_: Hashable, number: str,
                 forward: Optional[bool] = False, operator: Optional[str] = 'any',
                 country: Optional[str] = 'RUS'):
        self.id = id_
        self.number = number
        self.service = service
        self.forward = forward
        self.operator = operator
        self.country = country

    @abc.abstractmethod
    async def set_activation_status(self, status: int):
        pass

    @property
    @abc.abstractmethod
    async def activation_code(self):
        pass

    def __hash__(self):
        return hash((self.id, self.number))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.id == other.id and self.number == other.id
