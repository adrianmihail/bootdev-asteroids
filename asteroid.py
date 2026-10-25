import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

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

    # if asteroid is hit by a shot, split itself into new ones
    def split(self) -> None:
        self.kill()

        # if the asteroid is a small one, then destroy it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # if not, then create 2 smaller asteroids
        else:
            log_event("asteroid_split")

            # create 2 new asteroids at random angles from the original
            # asteroid position
            random_angle = random.uniform(20,50)
            first_asteroid_movement = self.velocity.rotate(random_angle)
            second_asteroid_movement = self.velocity.rotate(-random_angle)

            smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            first_new_asteroid = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
            second_new_asteroid = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)

            first_new_asteroid.velocity = first_asteroid_movement * 1.2
            second_new_asteroid.velocity = second_asteroid_movement * 1.2
