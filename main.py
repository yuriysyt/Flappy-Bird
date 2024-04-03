import pygame
from func_image.find_img import img_spawn

class GameLoop:
    width, height = 1280,720
    running = False
    dt = 0

    def __init__(self):

        self.player_pos, self.ground_pos, self.tree_pos, self.sky_pos, self.tube_pos, self.background_pos, self.gameover_pos, self.welcome_pos = img_spawn(self.screen)


    def input(self):
        pass
                

    def game_loop(self):
        while self.running:
            pass


if __name__ == "__main__":
    game = GameLoop()
    game.game_loop()

pygame.quit()