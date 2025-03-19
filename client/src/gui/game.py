import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

from stateManager import StateManager
from states.home import *
from states.testState import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Karte")

        self.state_manager = StateManager('Home')
        self.home = Home(self.screen, self.state_manager)
        self.test_state = TestState(self.screen, self.state_manager)

        self.states = {'Home': self.home, 'Test': self.test_state}
    
    def run(self): 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.states[self.state_manager.get_state()].run()
            pygame.display.update()
            self.clock.tick(FPS)