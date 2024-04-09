from functions.calculations.score_calculator import ScoreCalculator
from levels.level_1 import maps
from func_image.find_img import images
import pygame
from functions.calculations.calculation import calculations
from functions.calculations.background_renderer import BackgroundRenderer
from functions.calculations.create_level import LevelRenderer

class DrawingTool():
    def draw(self):
        self.screen.fill('#4ec0ca')

        BackgroundRenderer.create_background(self)
        
        if self.is_jumping:
            self.screen.blit(images.upCarImg, self.player_pos)
        else:
            self.screen.blit(images.downCarImg, self.player_pos)

        for i in range(-2, 7):
            self.screen.blit(images.groundImg, (self.ground_pos.x + 300 * i, self.ground_pos.y))

        LevelRenderer.create_level(self)

        self.screen.blit(images.treeImg, self.tree_pos)

        if self.losing:
            image_rect = images.gameoverImg.get_rect()
            image_rect.center = self.gameover_pos
            self.screen.blit(images.gameoverImg, (image_rect.x, image_rect.y - 100))
            self.screen.blit(images.welcomeImg,(image_rect.x, image_rect.y))

        if self.winning:
            image_rect = images.winImg.get_rect()
            image_rect.center = self.gameover_pos
            self.screen.blit(images.winImg, (image_rect.x, image_rect.y - 100))
        
        font = pygame.font.SysFont(None, 48)
        score_text = font.render(ScoreCalculator.get_score(self), True, '#ffffff')
        self.screen.blit(score_text, (self.screen.get_width() - 100, 100))
       
        pygame.display.flip()
        self.clock.tick(300)