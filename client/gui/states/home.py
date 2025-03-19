import pygame

from states.abstractState import AbstractState

from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, GRAY, BLACK
from buttons import draw_button
from utils import FONT

class Home(AbstractState):
    def run(self):
        button_width = 200
        button_height = 50

        play_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 - button_height - 20, button_width, button_height)

        self.display.fill(WHITE)
        welcome_text = "SALAM LES KHOYAS"
        textobj = FONT.render(welcome_text, True, BLACK)
        textrect = textobj.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        self.display.blit(textobj, textrect)
        draw_button(self.display, GRAY, play_button, "Play")

        pos = pygame.mouse.get_pos()

        if play_button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.state_manager.set_state("Test")