from game_object import GameObject
from movable import Movable

class Snake(GameObject, Movable):
    def __init__(self, start_position):
        super().__init__(start_position)
        self.body = [start_position]  # Cuerpo de la serpiente es una lista de posiciones
        self.direction = (1, 0)  # Dirección inicial (derecha)
        self.grow_pending = False

    def move(self):
        """Mueve la serpiente en la dirección actual."""
        new_head = [self.body[0][0] + self.direction[0] * 20, self.body[0][1] + self.direction[1] * 20]
        self.body.insert(0, new_head)
        if not self.grow_pending:
            self.body.pop()  
        else:
            self.grow_pending = False

    def grow(self):
        """Activa el crecimiento de la serpiente."""
        self.grow_pending = True

    def change_direction(self, key):
        """Cambia la dirección de la serpiente basada en la entrada."""
        if key == "UP" and self.direction != (0, 1):
            self.direction = (0, -1)
        elif key == "DOWN" and self.direction != (0, -1):
            self.direction = (0, 1)
        elif key == "LEFT" and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif key == "RIGHT" and self.direction != (-1, 0):
            self.direction = (1, 0)

    def head_collides_with(self, position):
        """Verifica si la cabeza de la serpiente colisiona con la posición dada."""
        return self.body[0] == position

    def collides_with_itself(self):
        """Verifica si la serpiente colisiona consigo misma."""
        return self.body[0] in self.body[1:]

    def is_out_of_bounds(self, width, height):
        """Verifica si la serpiente está fuera de los límites del display."""
        head = self.body[0]
        return not (0 <= head[0] < width and 0 <= head[1] < height)