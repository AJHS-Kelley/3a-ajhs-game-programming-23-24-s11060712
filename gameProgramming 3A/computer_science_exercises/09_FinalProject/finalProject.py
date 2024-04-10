# Ariel Combat Sim, Gavin Kloeckner, v0.1

import pygame
from sys import exit
from random import randint   

pygame.init()
screen = pygame.display.set_mode((1000,900))
pygame.display.set_caption('Soar')
clock = pygame.time.Clock()
screen.fill('Light Blue')
test_font = pygame.font.Font(None, 198)

text_surface = test_font.render('Soar', False, 'Green')

mig_surface = pygame.image.load()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(90)

    screen.blit(text_surface, (340,290))


