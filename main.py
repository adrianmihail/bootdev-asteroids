import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state

def main():
    # Welcome screen
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Init game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

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

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
