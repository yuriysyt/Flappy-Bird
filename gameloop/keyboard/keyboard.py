from gameloop.keyboard.event import EventHandling
from gameloop.keyboard.input import InputHandling

"""
This is the execution of the event.py and input.py files
"""
class KeyboardManager:
    def handle_keyboard(self):
        EventHandling.handle_events(self)
        InputHandling.handle_input(self)
