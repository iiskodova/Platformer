import pygame
from GameManager import GameManager
pygame.init()

PLAYER_VEL = 7
WIDTH, HEIGHT = 1200, 800
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    '''loads player character, takes care about movement and character animation '''
    GRAVITY = 1
    SPRITES = GameManager.load_sprite_sheets('MainCharacters', 'MaskDude', 32, 32, True)
    #change 'MaskDude' to get another character
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        # says how fast will the object move in x,y directions
        self.mask = None
        self.direction = 'left'
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != 'left':
            self.direction = 'left'
            self.animation_count = 0
  
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != 'right':
            self.direction = 'right'
            self.animation_count = 0
    
    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
    
    def hit_head(self):
        self.hit_head_count = 0
        self.y_vel *= -1

    def make_hit(self):
        self.hit = True
        self.hit_count = 0


    def loop(self, fps):
        '''is called once per frame(=iteration of the while loop)
        moves the character in chosen direction
        updates animation'''

        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        # this line makes the character fall down, imitates Earth gravity 
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count +=1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count +=1
        self.update_sprite()
    
    def update_sprite(self):
        sprite_sheet = 'idle'
        if self.hit:
            sprite_sheet = 'hit'
        if self.x_vel != 0:
            sprite_sheet = 'run'
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = 'jump'
            elif self.jump_count == 2:
                sprite_sheet = 'double_jump'
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = 'fall'


        sprite_sheet_name = sprite_sheet + '_' + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        #updating the rectangle of our character according 
        #to the dimensions of the sprite we use
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))

        #mask for pixel perfect collision
        self.mask = pygame.mask.from_surface(self.sprite)
    
    
    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))