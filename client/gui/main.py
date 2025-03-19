import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from screens import welcome_screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Karte")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        welcome_screen(screen)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()