import unittest
import unittest.mock
import pygame

# Import the necessary modules and classes from your game code
from gameloop.game_loop import GameLoop
from gameloop.calculations.calculation import Calculations
from gameloop.calculations.jump import JumpCalculator
from gameloop.calculations.lose_game import CollisionDetector
from gameloop.calculations.score_calculator import ScoreCalculator
from levels import level_1
from menu.actions.options_manager import LevelOptionsUpdater

class TestFlappyBird(unittest.TestCase):
    def setUp(self):
        # Initialize the game loop with a test level and selected_option
        self.game_loop = GameLoop(LevelOptionsUpdater.update_options(1), 2)  # Assuming the selected_option is required
        # Initialize other necessary attributes directly here
        self.game_loop.player_pos = [0, 0]  # Example initialization, replace with actual initialization
        self.game_loop.ground_pos = [0, 0]  # Example initialization, replace with actual initialization
        self.game_loop.tree_pos = [0, 0]  # Example initialization, replace with actual initialization

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
        # Assuming jump duration is constant and known
        pygame.time.wait(100)  # Wait for jump duration
        self.assertTrue(initial_y > self.game_loop.player_pos[1])

    def test_game_over_collision(self):
        test_rect = pygame.Rect(0, 0, 100, 100)
        self.game_loop.losing = False
        CollisionDetector.lose_game(self.game_loop, test_rect, [50, 50])
        self.assertTrue(self.game_loop.losing)

    def test_game_over_out_of_bounds(self):
        self.game_loop.losing = False
        # Move player out of bounds
        self.game_loop.player_pos = [-100, -100]
        Calculations.calculate(self.game_loop)
        self.assertTrue(self.game_loop.losing)

    def test_level_completion(self):
        self.game_loop.winning = False
        # Assuming reaching finish_ticks should trigger winning
        self.game_loop.path_to_selected_level.finish_ticks = 1
        Calculations.calculate(self.game_loop)
        self.assertTrue(self.game_loop.winning)


if __name__ == '__main__':
    unittest.main()
