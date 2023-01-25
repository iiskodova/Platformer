import pygame
pygame.init()

PLAYER_VEL = 7

class HandleMovement():
    def handle_vertical_collision(player, objects, displacement_y):
        collided_objects = []
        for object in objects:
            if pygame.sprite.collide_mask(player, object):
                if displacement_y > 0:
                    player.rect.bottom = object.rect.top
                    player.landed()
                elif displacement_y < 0:
                    player.rect.top = object.rect.bottom
                    player.hit_head()
            
                collided_objects.append(object)
    
        return collided_objects

    def handle_horizontal_collision(player, objects, displacement_x):
        player.move(displacement_x, 0)
        player.update()
        collided_object = None
        for object in objects:
            if pygame.sprite.collide_mask(player, object):
                collided_object = object
                break
        
        player.move(-displacement_x, 0)
        player.update()
        return collided_object



    def handle_move(player, objects):
        keys = pygame.key.get_pressed()

        player.x_vel = 0
        collide_left = HandleMovement.handle_horizontal_collision(player, objects, -PLAYER_VEL * 2)
        collide_right = HandleMovement.handle_horizontal_collision(player, objects, PLAYER_VEL * 2)
    
        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
    
        vertical_collide = HandleMovement.handle_vertical_collision(player, objects, player.y_vel)

        to_check = [collide_left, collide_right, *vertical_collide]
        for obj in to_check:
            if obj and obj.name == 'fire':
                player.make_hit()

