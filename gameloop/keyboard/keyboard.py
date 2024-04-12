from gameloop.keyboard.event import EventHandling
from gameloop.keyboard.input import InputHandling

class KeyboardManager:
    def handle_keyboard(self):
        EventHandling.handle_events(self)
        InputHandling.handle_input(self)
