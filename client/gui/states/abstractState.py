from abc import ABC, abstractmethod

class AbstractState(ABC):
    def __init__(self, display, state_manager):
        self.display = display
        self.state_manager = state_manager

    @abstractmethod
    def run(self):
        pass