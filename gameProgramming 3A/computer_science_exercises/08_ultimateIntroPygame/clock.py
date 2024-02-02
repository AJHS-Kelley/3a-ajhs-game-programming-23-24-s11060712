# Displaying Images on a Surface, Gavin Kloeckner, v0.0.6

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

ground_surface = pygame.image.load('graphics/red_stone.jpg').convert()
sky_surface = pygame.image.load('graphics/blue_sky.jpg').convert()
text_surface = test_font.render('My Game', True, 'Dark Green')

alligator_surface = pygame.image.load('graphics/Alligator.png').convert_alpha()
alligator_rect = alligator_surface.get_rect(bottomright = (600, 300))
alligator_x_pos = 800

player_surface = pygame.image.load('graphics/steve.png').convert_alpha()
player_x_pos = 200
player_rect = player_surface.get_rect(midbottom = (50,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    alligator_x_pos -= 3
    if alligator_x_pos < -300: alligator_x_pos = 800
    screen.blit(alligator_surface, alligator_rect)
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(80)
