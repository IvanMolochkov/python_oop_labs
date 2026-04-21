from abc import ABC, abstractmethod


class Calculate(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Printable(ABC):
    @abstractmethod
    def to_string(self):
        pass