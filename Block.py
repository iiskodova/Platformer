from GameObject import GameObject
from GameManager import GameManager
import pygame
pygame.init()

class Block(GameObject):
    '''draws block, sets dimensions'''
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        block = GameManager.load_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)