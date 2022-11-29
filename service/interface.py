from abc import ABC, abstractmethod
from typing import Tuple

class ClientInterface(ABC):
    @abstractmethod
    def connect(self):
        pass