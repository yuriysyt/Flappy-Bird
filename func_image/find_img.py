import pygame
import os

image_folder = os.path.join(os.path.dirname(__file__), 'images')

class images:
    backgroundImg = pygame.image.load(os.path.join(image_folder, "background.png"))
    flippyImg = pygame.image.load(os.path.join(image_folder, "flippy.png")) 
    flippyImg = pygame.transform.scale(flippyImg, (100, 60))
    downCarImg = pygame.transform.rotate(flippyImg, -45)
    upCarImg = pygame.transform.rotate(flippyImg, 45)
    gameoverImg = pygame.image.load(os.path.join(image_folder, "gameover.png"))
    winImg = pygame.image.load(os.path.join(image_folder, "win.png"))
    groundImg = pygame.image.load(os.path.join(image_folder, "ground.png"))
    skyImg = pygame.image.load(os.path.join(image_folder, "sky.png"))
    supermanImg = pygame.image.load(os.path.join(image_folder, "Superman.png"))
    textWrapperImg = pygame.image.load(os.path.join(image_folder, "text-wrapper.png"))
    treeImg = pygame.image.load(os.path.join(image_folder, "tree.png"))
    tubeImg = pygame.image.load(os.path.join(image_folder, "tube.png"))
    rotateTubeImg = pygame.transform.flip(tubeImg, False, True)
    welcomeImg = pygame.image.load(os.path.join(image_folder, "welcome.png"))

def img_spawn(screen):
    width_for_img, height_for_img = screen.get_width(), screen.get_height()
    player_pos = pygame.Vector2(width_for_img / 1000, height_for_img / 2)
    background_pos = pygame.Vector2(width_for_img / 1, height_for_img / 1)
    ground_pos = pygame.Vector2(width_for_img / 1500, height_for_img / 1.3)
    tree_pos = pygame.Vector2(width_for_img / 1.5, height_for_img / 1.7)
    sky_pos = pygame.Vector2(width_for_img / 400, height_for_img / 1500)
    gameover_pos = pygame.Vector2(width_for_img / 2, height_for_img / 2)
    win_pos = pygame.Vector2(width_for_img / 2, height_for_img / 2)
    tube_pos = pygame.Vector2(width_for_img / 1500, height_for_img / 1.3)
    welcome_pos = pygame.Vector2(width_for_img / 2, height_for_img / 2)


    return player_pos, ground_pos, tree_pos, sky_pos, tube_pos, background_pos, gameover_pos, welcome_pos, win_pos

