from abc import ABC, abstractmethod


class Option(ABC):
    name = '?'

    @abstractmethod
    async def run(self): pass
