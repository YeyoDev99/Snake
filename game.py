import pygame
from snake import Snake
from food import Food
from pygame_display import PygameDisplay  

class Game:
    def __init__(self):
        self.snake = Snake([100, 100])
        self.food = Food()
        self.display = PygameDisplay() 
        self.is_running = True

    def run(self):
        """Bucle principal del juego."""
        clock = pygame.time.Clock()

        while self.is_running:
            self._handle_events()
            self.snake.move()
            self._check_collisions()
            self.display.update(self.snake, self.food)
            clock.tick(10)  # Control de FPS (10 cuadros por segundo)

    def _handle_events(self):
        """Manejo de eventos del teclado."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def _check_collisions(self):
        """Verifica las colisiones de la serpiente."""
        if self.snake.head_collides_with(self.food.position):
            self.snake.grow()
            self.food.relocate(self.snake.body)

        if self.snake.collides_with_itself() or self.snake.is_out_of_bounds(self.display.WIDTH, self.display.HEIGHT):
            print("Game Over!")
            self.is_running = False
