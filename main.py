from unittest.loader import defaultTestLoader

import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    # Welcome screen
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Init game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # Define FPS to draw 60 per second
    clock = pygame.time.Clock()
    dt = 0.0

    # Instantiate Player at Center of the Screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Create Game Loop
    while True:
        # Log the state of the game
        log_state()

        # Process the pygame event queue
        for event in pygame.event.get():
            # If you press the Close button, exit the instance
            if event.type == pygame.QUIT:
                return

        # Fill the screen with Black Color
        screen.fill("black")

        # Draw the player position
        player.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Calculate Delta Time
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
