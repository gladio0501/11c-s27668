import math
from abc import ABC, abstractmethod


class SquareGenerator(ABC):

    @abstractmethod
    def generate_squares(self,start, end):
        pass