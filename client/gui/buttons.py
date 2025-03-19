import pygame
from utils import FONT
from config import BLACK

def draw_button(surface, color, rect, text):
    pygame.draw.rect(surface, color, rect)

    # Calculate the center position for the text
    textobj = FONT.render(text, True, BLACK)
    textrect = textobj.get_rect(center=rect.center)

    # Draw the text onto the button
    surface.blit(textobj, textrect)