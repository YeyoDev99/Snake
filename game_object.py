class GameObject:
    def __init__(self, position):
        self.position = position
    
    def collides_with(self, other_position):
        """Devuelve True si las posiciones del objeto colisionan."""
        return self.position == other_position
