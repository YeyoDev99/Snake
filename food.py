from game_object import GameObject
import random

class Food(GameObject):
    def __init__(self):
        super().__init__([random.randint(0, 29) * 20, random.randint(0, 19) * 20])

    def relocate(self, snake_body):
        """Reubica la comida en una posición aleatoria que no esté ocupada por la serpiente."""
        while True:
            new_position = [random.randint(0, 29) * 20, random.randint(0, 19) * 20]
            if new_position not in snake_body:
                self.position = new_position
                break
