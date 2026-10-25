import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    # Init
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x,y,radius)

    # Draw the asteroid into the screen
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white",self.position,self.radius,LINE_WIDTH)

    # Update the position so it moves ina straight line at a constant speed
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
