# Displaying Images on a Surface, Gavin Kloeckner, v0.0.7

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

ground_surf = pygame.image.load('graphics/red_stone.jpg').convert()
sky_surf = pygame.image.load('graphics/blue_sky.jpg').convert()
text_surf = test_font.render('My Game', True, 'Dark Green')

alligator_surf = pygame.image.load('graphics/Alligator.png').convert_alpha()
alligator_rect = alligator_surf.get_rect(bottomright = (600, 300))
alligator_x_pos = 800

player_surf = pygame.image.load('graphics/steve.png').convert_alpha()
player_x_pos = 200
player_rect = player_surf.get_rect(midbottom = (50,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos): print('Collision Deteced!')


    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(text_surf, (300, 50))

    alligator_rect.x -= 3
    if alligator_rect.right <= 0: alligator_rect.left = 800
    screen.blit(alligator_surf, alligator_rect)
    screen.blit(player_surf, player_rect)

    # if player_rect.colliderect(alligator_rect):
    #     print('Collision Detected!')
    
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(80)
