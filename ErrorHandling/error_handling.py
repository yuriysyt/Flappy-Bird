"""
The ErrorHandler class contains functions to handle various errors 
that may occur during program execution.

handle_error: This function handles general errors by printing an error message 
along with the exception details.

game_loop_error_handler: Handles errors that occur during the game loop, 
providing a specific message for game-related issues.

menu_loop_error_handler: Handles errors that occur while navigating the menu, 
with a specific message tailored for menu-related errors.

main_error_handler: The main function for handling errors during program execution. 
It provides a catch-all error message for any unexpected issues.
"""

class ErrorHandler:

    # Function to handle errors
    def handle_error(error_message, exception):
        print(f"Oops! {error_message}: {exception}")

    # Function to handle errors in the game loop
    def game_loop_error_handler(exception):
        ErrorHandler.handle_error("Something went wrong during the game.", exception)

    # Function to handle errors in the menu loop
    def menu_loop_error_handler(exception):
        ErrorHandler.handle_error("Oops! Something went wrong while navigating the menu.", exception)

    # Main function to handle errors during program execution
    def main_error_handler(exception):
        ErrorHandler.handle_error("Oops! Something went wrong with the program.", exception)
