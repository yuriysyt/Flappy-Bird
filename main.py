from menu.menu import Menu
"""
A bit about my code.

In my code, everything unfolds with each method.
For example, the menu.py file calls all methods from the menu folder,
And the gameloop.py file calls all methods from the gameloop folder.

(These are the two main folders that then call everything in sequence, each element)

I also tried to divide it into a large number of classes and functions
So that it's clear what the code is doing at any given moment.
Each class and function is described in detail to improve code readability.
"""
"""
The beginning of my code, where I initialize the Menu class.
After that, I start the While Loop (Menu Loop)
Where the player can choose to start the game, select a level, or exit.
"""

if __name__ == "__main__":
    menu = Menu()
    menu.menu_loop()