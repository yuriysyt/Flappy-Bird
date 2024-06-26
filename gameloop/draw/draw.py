from gameloop.calculations.score_calculator import ScoreCalculator
from images.find_img import images
import pygame
from gameloop.calculations.background_renderer import BackgroundRenderer
from gameloop.calculations.create_level import LevelRenderer

"""
This class is used to draw our entire screen using calculations
(Data Visualization)
"""
class DrawingTool():
    def draw(self):
        self.screen.fill('#4ec0ca')

        BackgroundRenderer.create_background(self)
        
        self.screen.blit(images.upCarImg if self.is_jumping else images.downCarImg, self.player_pos)

        for i in range(-2, 7):
            self.screen.blit(images.groundImg, (self.ground_pos.x + 300 * i, self.ground_pos.y))

        LevelRenderer.create_level(self)

        self.screen.blit(images.treeImg, self.tree_pos)

        """
        If the player loses or wins, we display the corresponding image
        """

        if self.losing:
            self.fall_speed = 1
            self.gravity = 0.2
            image_rect = images.gameoverImg.get_rect()
            image_rect.center = self.gameover_pos
            self.screen.blit(images.gameoverImg, (image_rect.x, image_rect.y - 100))
            self.screen.blit(images.welcomeImg,(image_rect.x, image_rect.y))

        if self.winning:
            self.fall_speed = 1
            self.gravity = 0.2
            image_rect = images.winImg.get_rect()
            image_rect.center = self.gameover_pos
            self.screen.blit(images.winImg, (image_rect.x, image_rect.y - 100))

        """
        Generating a font to display the player's score using the ScoreCalculator class
        """
        
        font = pygame.font.SysFont(None, 48)
        score_text = font.render(ScoreCalculator.get_score(self), True, '#ffffff')
        self.screen.blit(score_text, (self.screen.get_width() - 100, 100))
       
        """
        And update our monitor, setting the FPS value
        """
        pygame.display.flip()
        self.clock.tick(300)
