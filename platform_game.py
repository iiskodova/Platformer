from trap import Fire
from character import Player
from pyramids import Background
from stone import Block
from move_manager import HandleMovement
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
        Block(-block_size, HEIGHT - block_size * 2, block_size),
        Block(-block_size, HEIGHT - block_size * 3, block_size),
        Block(-block_size, HEIGHT - block_size * 4, block_size),
        Block(-block_size, HEIGHT - block_size * 5, block_size),
        Block(-block_size, HEIGHT - block_size * 6, block_size),
        Block(-block_size, HEIGHT - block_size * 7, block_size),
        Block(-block_size, HEIGHT - block_size * 8, block_size),
        Block(-block_size, HEIGHT - block_size * 9, block_size),
        Block(block_size * 3, HEIGHT - block_size * 4, block_size),
        Block(block_size * 4, HEIGHT - block_size * 5, block_size), 
        Block(block_size * 5, HEIGHT - block_size * 5, block_size),
        Block(block_size * 7, HEIGHT - block_size * 5, block_size),
        Block(block_size * 7, HEIGHT - block_size * 4, block_size),
        Block(block_size * 5, HEIGHT - block_size * 3, block_size),
        Block(block_size * 6, HEIGHT - block_size * 3, block_size),
        Block(block_size * 7, HEIGHT - block_size * 7, block_size),
        Block(block_size * 7, HEIGHT - block_size * 8, block_size),
        Block(block_size * 7, HEIGHT - block_size * 9, block_size),
        Block(block_size * 8, HEIGHT - block_size * 3, block_size),
        Block(block_size * 10, HEIGHT - block_size * 4, block_size),
        Block(block_size * 10, HEIGHT - block_size * 3, block_size),
        Block(block_size * 10, HEIGHT - block_size * 2, block_size),
        Block(block_size * 11, HEIGHT - block_size * 2, block_size),
        Block(block_size * 12, HEIGHT - block_size * 5, block_size),
        Block(block_size * 13, HEIGHT - block_size * 5, block_size),
        Block(block_size * 14, HEIGHT - block_size * 5, block_size),
        Block(block_size * 15, HEIGHT - block_size * 5, block_size),
        Block(block_size * 16, HEIGHT - block_size * 5, block_size),
        Block(block_size * 18, HEIGHT - block_size * 8, block_size),
        Block(block_size * 18, HEIGHT - block_size * 7, block_size),
        Block(block_size * 18, HEIGHT - block_size * 6, block_size),
        Block(block_size * 18, HEIGHT - block_size * 5, block_size),
        Block(block_size * 18, HEIGHT - block_size * 4, block_size),
        Block(block_size * 17, HEIGHT - block_size * 3, block_size),
        Block(block_size * 16, HEIGHT - block_size * 3, block_size),
        Fire(180, HEIGHT - block_size - 64, 16, 32),
        Fire(220, HEIGHT - block_size - 64, 16, 32),
        Fire(260, HEIGHT - block_size - 64, 16, 32),
        Fire(300, HEIGHT - block_size - 64, 16, 32),
        Fire(340, HEIGHT - block_size - 64, 16, 32),
        Fire(730, 258, 16, 32),
        Fire(680, 258, 16, 32),
        Fire(1566, 258, 16, 32),
        ]

    # fire = Fire
    # fire.loop()

    offset_x = 0
    scroll_area_width = 200

    
    run = True
    while run:
        clock.tick(FPS) 
        # set the FPS so the game runs at the same speed on every device

        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        #Fire.loop()
        HandleMovement.handle_move(player, objects)
        Background.draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel <0):
            offset_x += player.x_vel

    pygame.quit()
    quit()
        
if __name__ == '__main__':
    main(window)