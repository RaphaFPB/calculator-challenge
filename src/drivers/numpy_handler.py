import numpy
from typing import List
from .interfaces.driver_handler_interface import DriverhandlerInterface

class NumpyHandler(DriverhandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def average(self, numbers: List[float]) -> float:
        return self.__np.average(numbers)