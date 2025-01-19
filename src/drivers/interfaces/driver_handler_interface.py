from abc import ABC, abstractmethod
from typing import List


class DriverhandlerInterface(ABC):

    @abstractmethod
    def average(self, numbers: List[float]) -> float:
        pass