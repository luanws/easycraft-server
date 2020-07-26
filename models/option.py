from abc import ABC, abstractmethod


class Option(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self): pass
