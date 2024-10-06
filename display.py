from abc import ABC, abstractmethod

class Display(ABC):

    @property
    @abstractmethod
    def WIDTH(self):
        pass

    @property
    @abstractmethod
    def HEIGHT(self):
        pass

    @abstractmethod
    def update(self, snake, food):
        """Dibuja la serpiente, la comida y actualiza la pantalla."""
        pass