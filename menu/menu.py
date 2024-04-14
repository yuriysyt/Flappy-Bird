import pygame
from gameloop.game_loop import GameLoop
from gameloop.screen.screen import DisplayManager
from pygame.locals import *
from .images.find_img import images

class Menu:
    def __init__(self):
        pygame.init()
        DisplayManager.init(self)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.options = ["Start Game", "Choose Level", "Quit"]
        self.selected_option = 0
        self.bird_img = images.flippyImg 
        self.bird_rect = self.bird_img.get_rect()
        self.bird_rect.centerx = 150
        self.bird_rect.centery = 290
        self.flap_timer = 0
        self.flap_interval = 10
        self.up = True

    def draw_menu(self):
        self.screen.fill('#4ec0ca')
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (250, 200 + i * 50))
        self.screen.blit(self.bird_img, self.bird_rect)

    def animate_bird(self):
        if pygame.time.get_ticks() - self.flap_timer > self.flap_interval:

            if self.up:
                self.bird_rect.centery -= 1.5
            else:
                self.bird_rect.centery += 1.4

            print(self.bird_rect.centery)

            if self.bird_rect.centery < 240:
                self.up = False
            elif self.bird_rect.centery > 290:
                self.up = True

            self.flap_timer = pygame.time.get_ticks()

    def menu_loop(self):
        while True:
            self.screen.fill((0, 0, 0))
            self.draw_menu()
            self.animate_bird()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == 0:
                            game = GameLoop()
                            game.game_loop()
                        elif self.selected_option == 1:
                            pass
                        elif self.selected_option == 2:
                            pygame.quit()
                            return

            self.clock.tick(30)