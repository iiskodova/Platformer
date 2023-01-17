import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

# GLOBAL VARIABLES  
WIDTH, HEIGHT = 1200, 800
FPS = 60
PLAYER_VEL = 8

window = pygame.display.set_mode((WIDTH, HEIGHT))

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]
    #loads every file inside the directory

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))
        
        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


class Player(pygame.sprite.Sprite):
    COLOR = (155, 0, 155)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
    #change "MaskDude" to get another character
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        # says how fast will the object move in x,y directions
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
  
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    def loop(self, fps):
        """is called once per frame(=iteration of the while loop)
        moves the character in chosen direction
        updates animation"""

        # self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        # this line makes the character fall down, imitates Earth gravity 
        self.move(self.x_vel, self.y_vel)

        self.fall_count +=1
        self.update_sprite()
    
    def update_sprite(self):
        sprite_sheet = "idle"
        if self.x_vel != 0:
            sprite_sheet = "run"
        
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1


    def draw(self, win):
        win.blit(self.sprite, (self.rect.x, self.rect.y))


def get_background(name):
    """calculates how many background tiles are needed 
    based on width and height of the tiles and game window"""

    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for w in range(WIDTH // width + 1):
        for h in range (HEIGHT // height + 1):
            pos = (w * width, h * height)
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image, player):
    """looping through tiles, drawing image at the position 
    filling entire screen with background images"""

    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)

    pygame.display.update()
    
def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Desert.png")
    #change .png to get different backgrounds

    player = Player(100, 100, 50, 50)

    run = True
    while run:
        clock.tick(FPS) 
        # set the FPS so the game runs at the same speed on every device

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()
        
if __name__ == "__main__":
    main(window)