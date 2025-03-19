from states.abstractState import AbstractState

class TestState(AbstractState):
    def run(self):
        self.display.fill("red")
