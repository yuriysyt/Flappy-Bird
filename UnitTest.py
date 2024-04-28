import unittest
import unittest.mock
import pygame


from gameloop.game_loop import GameLoop
from gameloop.calculations.calculation import Calculations
from gameloop.calculations.jump import JumpCalculator
from gameloop.calculations.lose_game import CollisionDetector
from gameloop.calculations.score_calculator import ScoreCalculator
from levels import level_1
from menu.actions.options_manager import LevelOptionsUpdater

"""
This test suite evaluates the functionality 
of the Flappy Bird game components.

setUp: Initializes the game loop with a test level and selected_option, 
and sets up other necessary attributes for testing.

test_init_positions: Verifies that initial positions for 
player, ground, and tree are not None.

test_jump: Tests the jump behavior by verifying 
that the player's vertical position decreases after a jump.

test_collision_detection: Tests collision detection 
by simulating a collision between the player and an obstacle.

test_score_calculation: Tests the calculation of the player's score 
based on the time elapsed since the start of the game.

test_init_attributes: Verifies that all required 
attributes are initialized in the game loop.

test_jump_duration: Tests the duration of a jump by verifying 
that the player's vertical position decreases over time during a jump.

test_game_over_collision: Tests game over condition 
due to collision with an obstacle.

test_game_over_out_of_bounds: Tests game over condition 
when the player moves out of bounds.

test_level_completion: Tests level completion condition 
when the player reaches the finish line.

"""

class TestFlappyBird(unittest.TestCase):
    def setUp(self):
        self.game_loop = GameLoop(LevelOptionsUpdater.update_options(1), 2)  
        self.game_loop.player_pos = [0, 0]  
        self.game_loop.ground_pos = [0, 0]  
        self.game_loop.tree_pos = [0, 0]  

    def test_init_positions(self):
        self.assertIsNotNone(self.game_loop.player_pos)
        self.assertIsNotNone(self.game_loop.ground_pos)
        self.assertIsNotNone(self.game_loop.tree_pos)

    def test_jump(self):
        initial_y = self.game_loop.player_pos[1]
        JumpCalculator.calculate_jump(self.game_loop)
        self.assertLess(self.game_loop.player_pos[1], initial_y)

    def test_collision_detection(self):
        test_rect = pygame.Rect(100, 100, 100, 100)
        CollisionDetector.lose_game(self.game_loop, test_rect, (150, 150))
        self.assertTrue(self.game_loop.losing)

    def test_score_calculation(self):
        self.game_loop.time_start_game = pygame.time.get_ticks() - 1000
        score = ScoreCalculator.get_score(self.game_loop)
        self.assertGreater(int(score), 900)
    
    def test_init_attributes(self):
        self.assertTrue(hasattr(self.game_loop, 'running'))
        self.assertTrue(hasattr(self.game_loop, 'path_to_selected_level'))
        self.assertTrue(hasattr(self.game_loop, 'player_pos'))
        self.assertTrue(hasattr(self.game_loop, 'ground_pos'))
        self.assertTrue(hasattr(self.game_loop, 'tree_pos'))
        self.assertTrue(hasattr(self.game_loop, 'background_pos'))
        self.assertTrue(hasattr(self.game_loop, 'tube_pos'))
        self.assertTrue(hasattr(self.game_loop, 'gameover_pos'))
        self.assertTrue(hasattr(self.game_loop, 'welcome_pos'))
        self.assertTrue(hasattr(self.game_loop, 'win_pos'))

    def test_jump_duration(self):
        initial_y = self.game_loop.player_pos[1]
        JumpCalculator.calculate_jump(self.game_loop)
        
        pygame.time.wait(100)  
        self.assertTrue(initial_y > self.game_loop.player_pos[1])

    def test_game_over_collision(self):
        test_rect = pygame.Rect(0, 0, 100, 100)
        self.game_loop.losing = False
        CollisionDetector.lose_game(self.game_loop, test_rect, [50, 50])
        self.assertTrue(self.game_loop.losing)

    def test_game_over_out_of_bounds(self):
        self.game_loop.losing = False
        
        self.game_loop.player_pos = [-100, -100]
        Calculations.calculate(self.game_loop)
        self.assertTrue(self.game_loop.losing)

    def test_level_completion(self):
        self.game_loop.winning = False
        
        self.game_loop.path_to_selected_level.finish_ticks = 1
        Calculations.calculate(self.game_loop)
        self.assertTrue(self.game_loop.winning)


if __name__ == '__main__':
    unittest.main()
