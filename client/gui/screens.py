import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, GRAY, BLACK
from buttons import draw_button
from utils import FONT

def welcome_screen(screen):
    button_width = 200
    button_height = 50

    create_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 - button_height - 20, button_width, button_height)
    join_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width // 2, SCREEN_HEIGHT // 2 + 20, button_width, button_height)

    screen.fill(WHITE)
    welcome_text = "SALAM LES KHOYAS"
    textobj = FONT.render(welcome_text, True, BLACK)
    textrect = textobj.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(textobj, textrect)
    draw_button(screen, GRAY, create_button, "Create Room")
    draw_button(screen, GRAY, join_button, "Join Room")

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if create_button.collidepoint(event.pos):
                print("Create Room button clicked")
            elif join_button.collidepoint(event.pos):
                print("Join Room button clicked")