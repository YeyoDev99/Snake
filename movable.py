from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self):
        """Mueve el objeto."""
        pass

    @abstractmethod
    def change_direction(self, key):
        """Cambia la dirección del objeto."""
        pass