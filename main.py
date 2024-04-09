import pygame
from func_image.find_img import images
from functions.calculations.calculation import calculations
from functions.draw import DrawingTool

class GameLoop:
    width, height = 1280,720
    running = False

    def __init__(self):

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        pygame.init()
        self.running = True   
        self.losing = False
        self.winning = False
        self.is_jumping = False
        self.current_time = pygame.time.get_ticks()
        self.time_start_game = pygame.time.get_ticks()
        self.last_score = 0
        self.down_time = 0  
        self.dt = self.clock.tick(60) / 1000
        self.gravity = 0.2
        self.jump_strength = -0.3
        self.fall_speed = 0.2

        self.player_pos, self.ground_pos, self.tree_pos, self.sky_pos, self.tube_pos, self.background_pos, self.gameover_pos, self.welcome_pos, self.win_pos = images.get_pos(self.screen)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and self.losing or self.winning:
                self.player_pos, self.ground_pos, self.tree_pos, self.sky_pos, self.tube_pos, self.background_pos, self.gameover_pos, self.welcome_pos, self.win_pos = images.get_pos(self.screen)
                self.time_start_game = pygame.time.get_ticks()
                self.losing, self.winning = False, False
                

    def game_loop(self):
        while self.running:
            self.input()
            calculations.calculate(self)
            DrawingTool.draw(self)


if __name__ == "__main__":
    game = GameLoop()
    game.game_loop()

pygame.quit()