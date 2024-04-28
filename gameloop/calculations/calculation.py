from FileHandling.file_handling import FileHandler
import pygame
from gameloop.calculations.init_pos import position
from gameloop.calculations.score_calculator import ScoreCalculator
from FileHandling.file_handling import FileHandler
from menu.actions.options_manager import LevelOptionsUpdater

"""
This class is created to perform minor calculations for the GameLoop
"""
class Calculations:
    """
    Initializes the variables

    position.init_object_position - gets the initial position of objects
    self.losing - sets the value to False, indicating the player has not lost yet
    self.winning - sets the value to False, indicating the player has not won yet
    self.is_jumping - variable to determine jumping when the user presses W
    self.running - sets the value to True to start the gameloop
    self.current_time - sets the current time
    self.time_start_game - sets the start time of the game (used for calculating game scores)
    self.clock - timer
    self.last_score - sets the value of the last score to 0
    self.dt - records the time elapsed since the previous frame
    self.gravity - determines the gravity value for our game
    self.jump_strength - jump strength when the user presses a button
    self.fall_speed - how fast the bird will fall when the user releases the button
    self.file_handler - used to save level progress to a file
    """

    def init(self):  
            position.init_object_position(self)
            self.losing = False
            self.winning = False
            self.is_jumping = False
            self.running = True
            self.current_time = pygame.time.get_ticks()
            self.time_start_game = pygame.time.get_ticks()
            self.clock = pygame.time.Clock() 
            self.last_score = 0
            self.dt = self.clock.tick(60) / 1000
            self.gravity = 0.2
            self.jump_strength = -0.3
            self.fall_speed = 0.2
            self.file_handler = FileHandler()
    
    """
    This function contains all the main calculations
    """
    def calculate(self):
        
        if not self.losing and not self.winning:

            """
            Here we determine the movement speed of all objects, the game speed
            For example, if we increase 5 by 10, then all objects will move very quickly backwards
            Consequently, the speed of the bird will increase
            """
            self.ground_pos[0] -= 5
            self.background_pos[0] -= 5
            self.sky_pos[0] -= 5
            self.tree_pos[0] -= 5
            self.tube_pos[0] -= 5

            """
            This condition is created for calculating the fall after the button is pressed

            When the user presses W, it takes 300 ticks, and then the bird starts to fall
            """
            if pygame.time.get_ticks() > self.current_time + 300:
                self.is_jumping = False

            """
            Condition to calculate winning the game, when the player wins

            If the current tick count is greater than the level configuration, then the player has won
            Then we set self.winning to True, indicating that the player has won

            Then we use self.file_handler to write the player's achievement to the file
             
            self.path_to_selected_level - increase the level by one and move on to its generation
            """
            if int(ScoreCalculator.get_score(self)) > self.path_to_selected_level.finish_ticks:
                self.winning = True
                self.file_handler.set_level_completed(self.path_to_selected_level.__module__, True)

                self.path_to_selected_level = LevelOptionsUpdater.update_options(self.selected_option + 1)
                self.selected_option += 1

            """
            Here in this condition, if the player falls under the map, 
            then make him a loser
            """

            if self.player_pos[1] < 0 or self.player_pos[1] > self.screen.get_width() - self.screen.get_width() / 4:
                self.losing = True

            """
            Condition to check if the clouds have gone out of view and are already at -600 on the X-axis
            Then we return it to its place
            """
            if self.sky_pos[0] < -600:
                self.sky_pos[0] = 0
            
            """
            Condition to check if the tree has gone out of view and is already at -300 on the X-axis
            Then we return it to its place
            """
            if self.tree_pos[0] < -300:
                self.tree_pos[0] = (self.screen.get_width()) + 50

            """
            Condition if the user has made a jump, then we raise his bird up
            Considering our gravity (self.dt)

            If the user starts falling, then we make the fall depending on gravity
            """
            if self.is_jumping:
                    self.player_pos[1] -= 50 * self.dt
                    self.fall_speed = 1
            else:
                self.fall_speed -= self.gravity
                self.player_pos[1] -= self.fall_speed
