import sys

class ErrorHandler:

    # Function to handle errors
    def handle_error(error_message, exception):
        print(f"Oops! {error_message}: {exception}")

    # Function to handle errors in the game loop
    def game_loop_error_handler(exception):
        ErrorHandler.handle_error("Something went wrong during the game. The game will stop now.", exception)
        sys.exit(1)

    # Function to handle errors in the menu loop
    def menu_loop_error_handler(exception):
        ErrorHandler.handle_error("Oops! Something went wrong while navigating the menu.", exception)

    # Main function to handle errors during program execution
    def main_error_handler(exception):
        ErrorHandler.handle_error("Oops! Something went wrong with the program.", exception)
        sys.exit(1)
