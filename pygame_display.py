import pygame
from display import Display  # La interfaz

class PygameDisplay(Display):
    WIDTH = 600
    HEIGHT = 400
    BACKGROUND_COLOR = (43, 64, 214)
    SNAKE_COLOR = (0, 255, 0)
    FOOD_COLOR = (255, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game")

    def update(self, snake, food):
        """Dibuja la serpiente, la comida y actualiza la pantalla."""
        self.screen.fill(self.BACKGROUND_COLOR)
        
        # Dibuja la serpiente
        for segment in snake.body:
            pygame.draw.rect(self.screen, self.SNAKE_COLOR, pygame.Rect(segment[0], segment[1], 20, 20))
        
        # Dibuja la comida
        pygame.draw.rect(self.screen, self.FOOD_COLOR, pygame.Rect(food.position[0], food.position[1], 20, 20))
        
        pygame.display.flip()