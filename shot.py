import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x:float, y:float) -> None:
        super().__init__(x,y,SHOT_RADIUS)

    # Draw the object into the screen
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white",self.position,self.radius,LINE_WIDTH)

    # Update the position so it moves in a straight line at a constant speed
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
