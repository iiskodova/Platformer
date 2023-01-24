import os
from os.path import join
import pygame
pygame.init()

WIDTH, HEIGHT = 1200, 800
FPS = 60
PLAYER_VEL = 7

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Background():
    def get_background(name):
        '''calculates how many background tiles are needed 
        based on width and height of the tiles and game window'''
    
        image = pygame.image.load(join('assets', 'Background', name))
        _, _, width, height = image.get_rect()
        tiles = []
    
        for w in range(WIDTH // width + 1):
            for h in range (HEIGHT // height + 1):
                pos = (w * width, h * height)
                tiles.append(pos)
    
        return tiles, image

    def draw(window, background, bg_image, player, objects, offset_x):
        '''looping through tiles, drawing image at the position 
        filling entire screen with background images'''
    
        for tile in background:
            window.blit(bg_image, tile)
    
        for object in objects:
            object.draw(window, offset_x)
    
        player.draw(window, offset_x)
    
        pygame.display.update()