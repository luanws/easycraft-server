from abc import ABC, abstractmethod


class Option(ABC):
    name = '?'

    @abstractmethod
    def run(self): pass
