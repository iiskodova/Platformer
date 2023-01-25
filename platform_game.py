from Fire import Fire
from Player import Player
from Background import Background
from Block import Block
from HandleMovement import HandleMovement
import pygame
pygame.init()

pygame.display.set_caption('Platformer')

# GLOBAL VARIABLES  
WIDTH, HEIGHT = 1200, 800
FPS = 60
PLAYER_VEL = 7

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()
    background, bg_image = Background.get_background('Desert.png')
    #change .png to get different backgrounds

    block_size = 96

    player = Player(100, 100, 50, 50)
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
    for i in range(-WIDTH // block_size, (WIDTH * 3) // block_size)]
    # blocks = [Block(0, HEIGHT - block_size, block_size)]


    objects = [
        *floor, 
        Block(0, HEIGHT - block_size * 2, block_size), 
        Block(0, HEIGHT - block_size * 7, block_size),
        Block(block_size * 3, HEIGHT - block_size * 4, block_size),
        Block(block_size * 4, HEIGHT - block_size * 5, block_size), 
        Block(block_size * 5, HEIGHT - block_size * 5, block_size),
        Block(block_size * 5, HEIGHT - block_size * 3, block_size),
        Block(block_size * 6, HEIGHT - block_size * 3, block_size),
        Block(block_size * 8, HEIGHT - block_size * 3, block_size),
        Block(block_size * 11, HEIGHT - block_size * 2, block_size),
        Block(block_size * 17, HEIGHT - block_size * 3, block_size),
        Block(block_size * 16, HEIGHT - block_size * 3, block_size)
    ]

    for x in range(12, 17):
        objects.append(Block(block_size * x, HEIGHT - block_size * 5, block_size))
    
    for y in range(2, 10):
        objects.append(Block(-block_size, HEIGHT - block_size * y, block_size))
    
    for y in range(4, 9):
        objects.append(Block(block_size * 18, HEIGHT - block_size * y, block_size))
    
    for y in range(4, 6):
        objects.append(Block(block_size * 7, HEIGHT - block_size * y, block_size))

    for y in range(7, 10):
        objects.append(Block(block_size * 7, HEIGHT - block_size * y, block_size))
    
    for y in range(2, 5):
        objects.append(Block(block_size * 10, HEIGHT - block_size * y, block_size))

    fires_coords = [
        (180, HEIGHT - block_size - 64),
        (220, HEIGHT - block_size - 64),
        (260, HEIGHT - block_size - 64),
        (300, HEIGHT - block_size - 64),
        (340, HEIGHT - block_size - 64),
        (730, 258),
        (680, 258),
        (1566, 258),
    ]

    fires = []
    for x, y in fires_coords:
        fires.append(Fire(x, y, 16, 32))

    objects += fires


    offset_x = 0
    scroll_area_width = 200

    
    run = True
    while run:
        clock.tick(FPS) 
        # set the FPS so the game runs at the same speed on every device

        for fire in objects[-8:]:
            fire.loop()
        
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)

        HandleMovement.handle_move(player, objects)
        Background.draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel <0):
            offset_x += player.x_vel

    pygame.quit()
    quit()
        
if __name__ == '__main__':
    main(window)
